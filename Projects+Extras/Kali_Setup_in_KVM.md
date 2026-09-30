
# Kali Linux Setup Guide for KVM

> Why KVM? KVM (Kernel-based Virtual Machine) gives near-native performance, but clipboard, display integration, and shared folders need explicit setup.

---

## Part 0: Host Prerequisites (Do This First)

Before creating the Kali VM, confirm your Linux host is ready:

1. CPU virtualization enabled in BIOS/UEFI (Intel VT-x or AMD-V).
2. KVM/libvirt stack installed (`qemu-kvm`, `libvirt-daemon-system`, `virt-manager`).
3. Your user is in `libvirt` and `kvm` groups.
4. `libvirtd` service is running.

Quick check commands on host:

```bash
egrep -c '(vmx|svm)' /proc/cpuinfo
sudo systemctl status libvirtd --no-pager
groups
```

---
## Network Overview

- **default** – a NAT network (`192.168.122.0/24`). Provides outbound Internet for the guest.
- **pentest‑lab** – an isolated lab network (`192.168.100.0/24`). Allows the guest to talk to the other vulnerable VMs.

These two NICs should be attached to the Kali VM (one to each network) to enable both Internet access and lab interaction.

## Network Configuration Steps

1. **Attach the NAT interface** (default network) – this provides Internet:

   ```bash
   virsh -c qemu:///system attach-interface Kali-Linux network default \
        --model virtio --config --live
   ```

2. **Attach the isolated lab interface** (`pentest-lab`) – this allows communication with the other vulnerable VMs:

   ```bash
   virsh -c qemu:///system attach-interface Kali-Linux network pentest-lab \
        --model virtio --config --live
   ```
   *If you created the VM with `virt-manager`, you can also add the interfaces via the UI:*
   - Open the Kali VM → **Details** → **NIC** → **Add Hardware** → **Network source:** choose `default` for the first NIC and `pentest‑lab` for the second.
   - Set **Device model** to `virtio` and check **`--config`** (to persist) and **`--live`** (to apply immediately).

3. **Verify the interfaces inside Kali** after reboot:

   ```bash
   ip a
   # You should see two interfaces, e.g.:
   # - ens3  (192.168.122.x) – NAT / Internet
   # - ens4  (192.168.100.x) – lab network
   ```

4. **Check routing** – the default route should point to the NAT interface:

   ```bash
   ip route
   # Expect a line like: default via 192.168.122.1 dev ens3
   ```

5. **Test connectivity**:

   ```bash
   ping -c 3 8.8.8.8        # Internet
   ping -c 3 192.168.100.1  # Lab gateway / another VM
   ```

These steps ensure that the Kali VM has both internet access and lab‑network connectivity, matching the behavior you would get with an Ubuntu guest.

## Part 1: Initial VM Creation

### Step 1: Create the Virtual Machine

| Setting                 | Recommended Value | Notes                                                    |
| ----------------------- | ----------------- | -------------------------------------------------------- |
| Installation Method     | ISO image         | Download from [kali.org](https://www.kali.org/get-kali/) |
| OS Type                 | Debian 12/13      | Select the closest match available                       |
| RAM                     | 8192 MiB (8 GB)   | Minimum 4 GB; 8 GB recommended for smooth operation      |
| CPU Cores               | 8 cores           | Adjust based on your host CPU                            |
| Disk Space              | 60-96 GiB         | 60 GiB minimum; 96 GiB if running multiple tools         |

---

## Part 2: Post-Installation Configuration (KVM-Specific)

### Phase A: Enable Clipboard and Display Integration

Install guest agents to enable clipboard sharing and automatic resizing:

```bash
sudo apt update && sudo apt install -y qemu-guest-agent spice-vdagent
sudo systemctl enable --now qemu-guest-agent
```

### Phase B: Set Up Shared Folder (Host <-> Guest)

Prefer `virtiofs` on modern KVM stacks (better performance and behavior). Keep `9p` as fallback.

1. In `virt-manager`, add Filesystem hardware:
   - Source: host path to share
   - Target: `kali_share`
   - Driver: use `virtiofs` when available, otherwise `virtio-9p`
2. Inside Kali, create mount point:

```bash
mkdir -p "$HOME/Desktop/SharedFolder"
```

3. Add ONE of these `fstab` entries (virtiofs first, 9p fallback):

```bash
# Preferred: virtiofs
echo "kali_share $HOME/Desktop/SharedFolder virtiofs defaults,nofail 0 0" | sudo tee -a /etc/fstab

# Fallback: 9p
echo "kali_share $HOME/Desktop/SharedFolder 9p trans=virtio,version=9p2000.L,rw,_netdev,nofail 0 0" | sudo tee -a /etc/fstab
```

4. Mount only the target path:

```bash
sudo mount "$HOME/Desktop/SharedFolder"
```

### Phase C: Enable 3D Acceleration and OpenGL

1. In `virt-manager` -> Display Spice, enable OpenGL.
2. Select the host render node. Do not hardcode the value; it differs by host.
3. In Video Virtio, enable 3D acceleration.

To list render nodes on host:

```bash
ls -l /dev/dri/renderD*
```

---

## Part 3: Universal Kali Setup Script

Save this as `kali-setup.sh`. It asks you to choose mode interactively (KVM or normal) before running setup.

```bash
#!/usr/bin/env bash
# ==============================================================================
# KALI SETUP SCRIPT (UNIVERSAL: KVM OR NORMAL)
# Safe, idempotent, and mode-aware.
# ==============================================================================
set -euo pipefail

# --- CONFIGURATION FLAGS ---
INSTALL_BASIC_TOOLS=true
INSTALL_SECURITY_TOOLS=true
INSTALL_NODE_NVM=true
INSTALL_SHELL_CONFIG=true

# --- SHARED FOLDER CONFIG ---
SHARE_TAG="kali_share"
SHARE_MOUNT_POINT="$HOME/Desktop/SharedFolder"

# --- COLORS / STATE ---
RED='\033[0;31m'; GREEN='\033[0;32m'; YELLOW='\033[1;33m'; BLUE='\033[0;34m'; NC='\033[0m'
STEP_TOTAL=0; STEP_PASS=0; STEP_SKIP=0; STEP_FAIL=0
CURRENT_STEP=""
SUDO_PID=""

log_info()  { echo -e "${GREEN}[OK]${NC} [$(date '+%H:%M:%S')] $1"; }
log_warn()  { echo -e "${YELLOW}[WARN]${NC} [$(date '+%H:%M:%S')] $1"; }
log_error() { echo -e "${RED}[ERR]${NC} [$(date '+%H:%M:%S')] $1"; }

retry() {
    local n=1 max=3 delay=5
    while true; do
        "$@" && return 0
        if (( n >= max )); then return 1; fi
        log_warn "Attempt $n/$max failed. Retrying in ${delay}s..."
        sleep "$delay"
        ((n++))
    done
}

start_step() {
    STEP_TOTAL=$((STEP_TOTAL + 1))
    CURRENT_STEP="$1"
    echo -e "\n${BLUE}>>> [STEP $STEP_TOTAL] $CURRENT_STEP${NC}"
}

pass_step() { STEP_PASS=$((STEP_PASS + 1)); }
skip_step() { STEP_SKIP=$((STEP_SKIP + 1)); log_warn "Skipped: $CURRENT_STEP"; }
on_error()  { STEP_FAIL=$((STEP_FAIL + 1)); log_error "Failed: $CURRENT_STEP"; }

ensure_line_in_file() {
    local line="$1"
    local file="$2"
    grep -Fqx "$line" "$file" || echo "$line" | sudo tee -a "$file" >/dev/null
}

cleanup() {
    if [[ -n "$SUDO_PID" ]]; then
        kill "$SUDO_PID" 2>/dev/null || true
    fi
}

trap 'on_error' ERR
trap cleanup EXIT

# --- LOGGING (SECURE PERMISSIONS) ---
sudo -v
LOG_FILE="/var/log/kali-setup.log"
sudo touch "$LOG_FILE"
sudo chown root:root "$LOG_FILE"
sudo chmod 600 "$LOG_FILE"
exec > >(tee -a "$LOG_FILE") 2>&1

# Keep sudo token alive in background.
while true; do sudo -n true; sleep 55; done 2>/dev/null &
SUDO_PID=$!

# --- MODE SELECTION (MANUAL) ---
echo -e "${BLUE}=============================================${NC}"
echo -e "${BLUE}      Kali Setup - Choose Installation Mode  ${NC}"
echo -e "${BLUE}=============================================${NC}"
echo "  1) KVM guest setup"
echo "  2) Normal setup (hardware/laptop/VPS)"
while true; do
    read -rp "Select mode [1/2]: " SETUP_CHOICE
    case "$SETUP_CHOICE" in
        1)  SETUP_MODE="kvm"; break ;;
        2)  SETUP_MODE="normal"; break ;;
        *)  log_warn "Invalid choice. Please enter 1 or 2." ;;
    esac
done

log_info "Using setup mode: $SETUP_MODE"

# --- SHARED ALIASES ---
SHARED_ALIASES='
# --- Custom Aliases ---
alias ls="eza --icons --group-directories-first"
alias ll="eza -la --icons --group-directories-first"
alias lt="eza --tree --icons --level=2"
alias cat="batcat --paging=never"
alias fd="fdfind"
alias help="tldr"
alias ports="ss -tulpn"
'

start_step "System Update"
retry sudo apt update
retry sudo apt upgrade -y
pass_step

start_step "Base Tools"
if [[ "$INSTALL_BASIC_TOOLS" == true ]]; then
    sudo apt install -y \
        zsh git curl vim fzf bat eza htop tree jq \
        python3-pip python3-venv pipx zoxide fonts-powerline mesa-utils
    
    if ! sudo apt install -y tldr; then
        log_warn "apt install tldr failed, attempting pip install..."
        pipx install tldr
    fi
    pass_step
else
    skip_step
fi

start_step "Platform Specifics (Mode: $SETUP_MODE)"
if [[ "$SETUP_MODE" == "kvm" ]]; then
    log_info "Installing guest agents..."
    sudo apt install -y qemu-guest-agent spice-vdagent
    sudo systemctl enable --now qemu-guest-agent

    log_info "Checking 3D acceleration hints..."
    if command -v glxinfo >/dev/null 2>&1; then
        if glxinfo 2>/dev/null | grep -Eiq 'virgl|llvmpipe|mesa'; then
            log_info "OpenGL renderer info is available."
        else
            log_warn "Could not verify accelerated renderer from glxinfo output."
        fi
    else
        log_warn "glxinfo not found (mesa-utils missing). Skipping renderer check."
    fi

    log_info "Configuring shared folder mount..."
    mkdir -p "$SHARE_MOUNT_POINT"

    if grep -qw virtiofs /proc/filesystems; then
        # x-gvfs-hide prevents GUI file managers (like Thunar) from creating dummy phantom icons in the sidebar
        FSTAB_LINE="$SHARE_TAG $SHARE_MOUNT_POINT virtiofs defaults,x-gvfs-hide,nofail 0 0"
        log_info "Using virtiofs for shared folder."
    else
        FSTAB_LINE="$SHARE_TAG $SHARE_MOUNT_POINT 9p trans=virtio,version=9p2000.L,rw,_netdev,nofail 0 0"
        log_warn "virtiofs unavailable; using 9p fallback."
    fi

    ensure_line_in_file "$FSTAB_LINE" /etc/fstab
    sudo mount "$SHARE_MOUNT_POINT" || log_warn "Mount failed. Verify virt-manager filesystem target and driver."
else
    log_info "Skipping KVM-specific agents and shared folder setup."
fi
pass_step

start_step "Kali Security Tools"
if [[ "$INSTALL_SECURITY_TOOLS" == true ]]; then
    sudo apt install -y seclists wordlists nmap metasploit-framework gobuster sqlmap
    if [[ -f /usr/share/wordlists/rockyou.txt.gz ]]; then
        sudo gunzip -f /usr/share/wordlists/rockyou.txt.gz
    fi
    pass_step
else
    skip_step
fi

start_step "Node via NVM"
if [[ "$INSTALL_NODE_NVM" == true ]]; then
    curl -fsSL https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.7/install.sh | bash
    export NVM_DIR="$([ -d "$HOME/.config/nvm" ] && echo "$HOME/.config/nvm" || echo "$HOME/.nvm")"
    # shellcheck disable=SC1090
    [ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"
    nvm install --lts
    pass_step
else
    skip_step
fi

start_step "Zsh + Oh My Zsh"
if [[ "$INSTALL_SHELL_CONFIG" == true ]]; then
    if [[ ! -d "$HOME/.oh-my-zsh" ]]; then
        RUNZSH=no CHSH=no KEEP_ZSHRC=yes sh -c "$(curl -fsSL https://raw.githubusercontent.com/ohmyzsh/ohmyzsh/master/tools/install.sh)" "" --unattended
    fi

    # Install external plugins to prevent "plugin not found" warnings.
    ZSH_CUSTOM="${ZSH_CUSTOM:-$HOME/.oh-my-zsh/custom}"
    [[ -d "$ZSH_CUSTOM/plugins/zsh-autosuggestions" ]] || git clone --depth=1 https://github.com/zsh-users/zsh-autosuggestions "$ZSH_CUSTOM/plugins/zsh-autosuggestions"
    [[ -d "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting" ]] || git clone --depth=1 https://github.com/zsh-users/zsh-syntax-highlighting "$ZSH_CUSTOM/plugins/zsh-syntax-highlighting"
    [[ -d "$ZSH_CUSTOM/plugins/zsh-history-substring-search" ]] || git clone --depth=1 https://github.com/zsh-users/zsh-history-substring-search "$ZSH_CUSTOM/plugins/zsh-history-substring-search"
    [[ -d "$ZSH_CUSTOM/plugins/zsh-completions" ]] || git clone --depth=1 https://github.com/zsh-users/zsh-completions "$ZSH_CUSTOM/plugins/zsh-completions"

    sed -i 's|^plugins=.*|plugins=(git sudo fzf z extract dirhistory copypath copyfile history command-not-found zsh-autosuggestions zsh-completions zsh-history-substring-search zsh-syntax-highlighting)|' "$HOME/.zshrc"
    grep -q "SHARED_ALIASES" "$HOME/.zshrc" || echo -e "\n# SHARED_ALIASES\n$SHARED_ALIASES" >> "$HOME/.zshrc"
    pass_step
else
    skip_step
fi

start_step "Python pipx Tools"
pipx ensurepath
declare -a PIPX_TOOLS=("impacket" "pwntools" "volatility3" "netexec")
for tool in "${PIPX_TOOLS[@]}"; do
    log_info "Installing $tool via pipx..."
    pipx install "$tool" || log_warn "$tool install failed or already installed."
done
pass_step

echo
log_info "Setup finished. Passed: $STEP_PASS | Skipped: $STEP_SKIP | Failed: $STEP_FAIL"
log_info "Log file: $LOG_FILE"
log_info "Mode used: $SETUP_MODE"
log_info "Recommended next step: reboot the VM."
```

### Notes

1. This script is safe to rerun; it avoids duplicate `fstab` entries.
2. The script always uses your manual mode selection (KVM or normal).
3. If shared folder mount fails, verify target tag (`kali_share`) and driver type in `virt-manager`.

### Important: Fedora/SELinux Host Fix

If you are running Fedora on the host, SELinux will automatically block KVM (`virtiofsd`) from accessing the shared folder (resulting in an empty directory or "Permission denied" errors inside the guest). 

You MUST run this command on your **Host System (Fedora)** to fix the security context of the folder before using the share:
```bash
sudo chcon -R -t svirt_image_t /home/smilo/Desktop/SharedFolder
```
