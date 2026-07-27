here i learn by doing thm module windows fundamental 1 and 2

# PowerShell Basics

## What is PowerShell?

- **PowerShell** is Microsoft's advanced command-line shell and scripting language built on the **.NET Framework/.NET**.
- It is more powerful than **Command Prompt (CMD)** because it works with **objects** instead of plain text.
- You can launch PowerShell from CMD by running:

  ```powershell
  powershell
  ```

  or, in newer versions:

  ```powershell
  pwsh
  ```

---

## Common PowerShell Commands

- **`Get-Command`** – Lists all available PowerShell commands.
- **`Get-Help <command>`** – Displays help and usage information for a command.
- **`Get-Date`** – Shows the current date and time.
- **`Get-Alias`** – Lists all command aliases (shortcuts) available in PowerShell.

---

## Finding & Installing Modules

- **`Find-Module`** – Searches the PowerShell Gallery for modules.

  ```powershell
  Find-Module -Name PowerShellGet
  ```

- **`Install-Module`** – Downloads and installs a PowerShell module.

  ```powershell
  Install-Module ModuleName
  ```

> Think of **`Install-Module`** as similar to a package manager for PowerShell modules.

---

# File & Directory Management

- **`Get-ChildItem` (`gci`, `ls`)** – Lists files and folders.
- **`Set-Location` (`cd`)** – Changes the current directory.
- **`New-Item`** – Creates a new file or folder.
- **`Remove-Item`** – Deletes files or folders (similar to Linux `rm`/`rmdir`).
- **`Copy-Item`** – Copies files or folders.
- **`Get-Content`** – Displays the contents of a file (similar to Linux `cat` or CMD `type`).

---

# PowerShell Pipeline (`|`)

- The **pipeline (`|`)** passes the **output (objects)** of one command as the **input** to another command.
- Unlike CMD, PowerShell passes **structured objects**, making filtering and sorting much more powerful.

### Common Pipeline Commands

### `Sort-Object`

Sorts objects by a property.

```powershell
Get-ChildItem | Sort-Object Length
```

Sorts files by their **size (`Length`)**.

---

### `Where-Object`

Filters objects based on a condition.

```powershell
Get-ChildItem | Where-Object Length -gt 1MB
```

Common comparison operators:

- `-eq` → Equal
- `-ne` → Not Equal
- `-gt` → Greater Than
- `-ge` → Greater Than or Equal
- `-lt` → Less Than
- `-le` → Less Than or Equal
- `-like` → Pattern matching
- `-notlike` → Does not match pattern

---

# `Select-Object`

**Purpose:** Displays only the properties or number of objects you want.

Example:

```powershell
Get-Process | Select-Object Name, Id
```

Output:

- Process Name
- Process ID

Instead of showing every property, it displays **only the selected ones**.

### How do you know which properties are available?

Use:

```powershell
<command> | Get-Member
```

Example:

```powershell
Get-Process | Get-Member
```

`Get-Member` lists **all properties and methods** of the objects returned by a command. Once you know the property names, you can use them with `Select-Object`, `Sort-Object`, or `Where-Object`.

Other useful examples:

```powershell
Get-ChildItem | Get-Member
```

```powershell
Get-Service | Get-Member
```

---

# `Select-String`

**Purpose:** Searches for specific text or patterns inside one or more files (similar to Linux `grep`).

Example:

```powershell
Select-String "password" users.txt
```

This searches for the word **"password"** inside `users.txt`.

Search multiple files:

```powershell
Select-String "admin" *.txt
```

Pipeline example:

```powershell
Get-Content users.txt | Select-String "admin"
```

This:

1. Reads the file using `Get-Content`.
2. Sends each line to `Select-String`.
3. Displays only the lines containing **"admin"**.

> **Key Difference:**
>
> - **`Select-Object`** → Selects **properties or objects** from command output.
> - **`Select-String`** → Searches for **text patterns** inside files or command output.
