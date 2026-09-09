# 📦 ELK Stack (Elastic Stack): Complete Mastery Checklist

> **What is the ELK Stack?** ELK is an acronym for three open-source tools built by Elastic: **Elasticsearch** (distributed search and analytics engine), **Logstash** (data ingestion and transformation pipeline), and **Kibana** (visualization and dashboarding UI). Together they form a powerful, open-source SIEM and log analytics platform. The modern term is **Elastic Stack**, as Beats (lightweight data shippers) are now a core component alongside the original three.
>
> **Why does it exist?** Organizations needed a scalable, open-source alternative to expensive proprietary SIEMs. Elasticsearch's inverted index architecture enables sub-second full-text search across billions of log events. Kibana makes that data explorable visually. It is the dominant open-source SIEM foundation globally.
>
> **When to use it:** As your SIEM in a self-hosted lab (free, no ingestion limits), when Splunk licensing is not available, for production log management in DevSecOps pipelines, and as the backend for many open-source security tools (Wazuh uses it as its storage engine).
>
> **When to avoid it:** ELK is complex to configure, tune, and scale. For a simple single-machine lab, Wazuh (which ships pre-configured ELK) is easier. For quick one-off log analysis, use `grep`/`jq`. For paid enterprise SIEM with pre-built correlation rules, Splunk ES is more mature.
>
> **What mastering ELK unlocks:** SOC operations capability, ability to deploy a SIEM from scratch, KQL (Kibana Query Language) proficiency, detection engineering using Elastic Security's SIEM rules, and understanding of the data pipeline architecture used in almost every enterprise SOC.
>
> **Roadmap Stage / Module:** Stage 3: Side-Track A (Detection Engineering & SOC Operations)

---

## 🧭 Navigation

> [🏠 Master Roadmap](../README.md) · [🔧 Tools Index](README.md)

| SIEM Platforms | Telemetry | Detection Rules | Forensics |
|:--------------|:----------|:----------------|:----------|
| [📊 Splunk](Splunk.md) | [🔭 Sysmon](Sysmon.md) | [🔎 Sigma](Sigma.md) | [🧠 Volatility](Volatility.md) |
| [🐺 Wazuh](Wazuh.md) | [📦 Plaso](Plaso.md) | [🦠 YARA](YARA.md) | [🔬 Autopsy](Autopsy.md) |
| **📦 ELK** (you are here) | | | |

---

## 📊 Progress Overview

| Phase | Focus | Tasks | Est. Time |
|:---:|:---|:---:|:---:|
| 1 | Installation & Stack Setup | 6 | 3–4 hours |
| 2 | Elasticsearch Core Concepts | 7 | 3–4 hours |
| 3 | Logstash Pipelines & Beats | 6 | 3–4 hours |
| 4 | Kibana & KQL Querying | 8 | 4–5 hours |
| 5 | Elastic Security (SIEM Module) | 7 | 4–6 hours |
| 6 | Sysmon + Winlogbeat Integration | 5 | 3–4 hours |
| 7 | Practical Labs | 4 | 6–8 hours |
| | **Total** | **43** | **~26–35 hours** |

**Prerequisites:** Linux fundamentals (Phase 1). Basic understanding of JSON. Docker knowledge is helpful (Docker Compose is the easiest install method).

---

# PHASE 1: INSTALLATION & STACK SETUP

---

## 1.1 Quick Start with Docker Compose (Recommended for Labs)

```bash
# Clone the official Elastic Docker Compose project
git clone https://github.com/elastic/elasticsearch-labs
# OR use the Elastic stack Docker Compose from elastic.co

# Minimal docker-compose.yml for ELK lab
cat > docker-compose.yml << 'EOF'
version: '3.8'
services:
  elasticsearch:
    image: docker.elastic.co/elasticsearch/elasticsearch:8.11.0
    environment:
      - discovery.type=single-node
      - xpack.security.enabled=false
      - ES_JAVA_OPTS=-Xms1g -Xmx1g
    ports:
      - "9200:9200"
    volumes:
      - esdata:/usr/share/elasticsearch/data

  kibana:
    image: docker.elastic.co/kibana/kibana:8.11.0
    ports:
      - "5601:5601"
    depends_on:
      - elasticsearch

  logstash:
    image: docker.elastic.co/logstash/logstash:8.11.0
    ports:
      - "5044:5044"
      - "9600:9600"
    volumes:
      - ./logstash/pipeline:/usr/share/logstash/pipeline

volumes:
  esdata:
EOF

docker compose up -d

# Verify Elasticsearch is up
curl http://localhost:9200
```

## 1.2 Manual Installation (Debian/Ubuntu)

```bash
# Add Elastic GPG key and repository
wget -qO - https://artifacts.elastic.co/GPG-KEY-elasticsearch | sudo apt-key add -
echo "deb https://artifacts.elastic.co/packages/8.x/apt stable main" | \
  sudo tee /etc/apt/sources.list.d/elastic-8.x.list

# Install all three
sudo apt update && sudo apt install elasticsearch kibana logstash

# Start services
sudo systemctl start elasticsearch kibana logstash
sudo systemctl enable elasticsearch kibana logstash

# Verify
curl http://localhost:9200
# Access Kibana: http://localhost:5601
```

- [ ] **Memory requirements:** Elasticsearch is memory-hungry. It uses a JVM heap — configure `ES_JAVA_OPTS=-Xms2g -Xmx2g` to allocate 2GB heap. Your lab VM should have at least 4GB RAM for ELK.
- [ ] **Disable swap:** Elasticsearch requires swap to be disabled for production performance: `sudo swapoff -a`
- [ ] **`vm.max_map_count`:** Elasticsearch requires `vm.max_map_count=262144`. Add `vm.max_map_count=262144` to `/etc/sysctl.conf` and run `sudo sysctl -p`.

---

# PHASE 2: ELASTICSEARCH CORE CONCEPTS

---

## 2.1 Key Elasticsearch Concepts

| Concept | Elasticsearch | SQL Equivalent |
|:--------|:-------------|:--------------|
| Cluster | Elasticsearch cluster | Database server |
| Index | Index | Database/table |
| Document | JSON document | Row |
| Field | Field in JSON doc | Column |
| Shard | Physical storage unit | Partition |
| Mapping | Field type definitions | Schema |

## 2.2 Elasticsearch REST API

```bash
# Check cluster health
curl http://localhost:9200/_cluster/health?pretty

# List all indices
curl http://localhost:9200/_cat/indices?v

# Create an index
curl -X PUT http://localhost:9200/logs-test-001

# Index a document
curl -X POST http://localhost:9200/logs-test-001/_doc/ \
  -H "Content-Type: application/json" \
  -d '{"timestamp":"2024-01-01T12:00:00","host":"web01","message":"SSH login failed for root"}'

# Search (match all)
curl http://localhost:9200/logs-test-001/_search?pretty

# Search with query DSL
curl -X POST http://localhost:9200/logs-test-001/_search?pretty \
  -H "Content-Type: application/json" \
  -d '{"query":{"match":{"message":"failed"}}}'

# Delete an index
curl -X DELETE http://localhost:9200/logs-test-001
```

## 2.3 Index Management

```bash
# View index settings and mapping
curl http://localhost:9200/logs-*/_mapping?pretty

# Aliases (abstract index names — important for ECS)
curl -X POST http://localhost:9200/_aliases \
  -H "Content-Type: application/json" \
  -d '{"actions":[{"add":{"index":"logs-2024.01","alias":"logs-current"}}]}'

# Index Lifecycle Management (ILM) — automated retention
# Configure via Kibana: Stack Management → Index Lifecycle Policies
```

- [ ] **ECS (Elastic Common Schema):** Elastic's field naming standard. All log sources should normalize to ECS fields: `@timestamp`, `host.name`, `source.ip`, `destination.ip`, `user.name`, `event.action`, `process.name`, `process.command_line`. Know the core ECS fields cold.
- [ ] **Data streams:** Modern Elastic SIEM uses data streams instead of plain indices. Data streams are append-only, time-series optimized, and auto-managed by ILM policies. Know the naming convention: `logs-<dataset>-<namespace>`.

---

# PHASE 3: LOGSTASH PIPELINES & BEATS

---

## 3.1 Logstash Pipeline Structure

Every Logstash pipeline has three sections:

```ruby
# /etc/logstash/conf.d/syslog.conf
input {
  beats {
    port => 5044   # Receive from Filebeat/Winlogbeat
  }
  syslog {
    port => 514    # Receive syslog directly
    type => "syslog"
  }
}

filter {
  if [type] == "syslog" {
    grok {
      match => { "message" => "%{SYSLOGTIMESTAMP:syslog_timestamp} %{SYSLOGHOST:syslog_hostname} %{DATA:syslog_program}: %{GREEDYDATA:syslog_message}" }
    }
    date {
      match => [ "syslog_timestamp", "MMM  d HH:mm:ss", "MMM dd HH:mm:ss" ]
    }
  }
  mutate {
    add_field => { "[@metadata][target_index]" => "logs-syslog-%{+YYYY.MM.dd}" }
  }
}

output {
  elasticsearch {
    hosts => ["http://localhost:9200"]
    index => "%{[@metadata][target_index]}"
  }
}
```

## 3.2 Beats — Lightweight Shippers

| Beat | Purpose | Use Case |
|:-----|:--------|:---------|
| **Filebeat** | Ships log files | syslog, app logs, audit logs |
| **Winlogbeat** | Ships Windows Event Logs | Windows endpoints in your lab |
| **Packetbeat** | Ships network packet data | Network monitoring |
| **Auditbeat** | Ships Linux audit framework data | Linux endpoint detection |
| **Metricbeat** | Ships system/service metrics | Performance monitoring |

```yaml
# filebeat.yml — forward syslog to Logstash
filebeat.inputs:
- type: log
  paths:
    - /var/log/auth.log
    - /var/log/syslog

output.logstash:
  hosts: ["localhost:5044"]

# winlogbeat.yml — Windows Event Logs to Elasticsearch
winlogbeat.event_logs:
  - name: Application
  - name: Security
    event_id: 4624, 4625, 4648, 4688, 4698, 4720

output.elasticsearch:
  hosts: ["http://elk-server:9200"]
  index: "winlogbeat-%{[agent.version]}-%{+yyyy.MM.dd}"
```

---

# PHASE 4: KIBANA & KQL QUERYING

---

## 4.1 Kibana Interface Overview

- **Discover:** Raw log browsing with KQL search, time filtering, field selection
- **Dashboard:** Build visualizations — bar charts, time series, geo maps, data tables
- **Alerts:** Create detection rules with thresholds and actions
- **Elastic Security (SIEM):** Dedicated security module with timelines, case management, and pre-built rules

## 4.2 KQL (Kibana Query Language)

```kql
# Basic keyword search
ssh AND failed

# Field-specific search
event.code : 4625

# Wildcard
process.name : *mimikatz*

# Range queries
event.code >= 4624 AND event.code <= 4625

# Exists check
user.name : *

# NOT operator
NOT source.ip : "10.0.0.0/8"

# Phrase matching (exact)
message : "failed password for root"

# Boolean combinations
(event.code : 4625 OR event.code : 4624) AND user.name : "administrator"
```

## 4.3 EQL (Event Query Language) — Sequence Detection

EQL is Elastic's language for detecting sequences of events (like Sigma for Splunk but native):

```eql
// Process injection sequence: process opens LSASS then reads memory
sequence by host.name
  [process where process.name == "*.exe" and
   process.pe.original_file_name != "lsass.exe"]
  [process where event.action == "open" and
   process.name == "lsass.exe"]
```

---

# PHASE 5: ELASTIC SECURITY (SIEM MODULE)

---

## 5.1 Enabling Elastic Security

1. Kibana → Main Menu → **Security**
2. This activates: Detection Rules, Timelines, Cases, Hosts, Network views
3. Install pre-built detection rules: Detection Rules → Add Elastic Rules → Install all ~700+ rules

## 5.2 Key Pre-Built Detection Rule Categories

```
- Windows:
  * Credential Access (LSASS dump, Mimikatz, SAM hive access)
  * Persistence (registry run keys, scheduled tasks, services)
  * Defense Evasion (process hollowing, timestomping)
  * Lateral Movement (PsExec, WMI, SMB lateral movement)

- Linux:
  * Privilege escalation via SUID/sudo abuse
  * Cron persistence
  * Unusual process ancestry

- Network:
  * DNS tunneling detection
  * Unusual outbound connections
  * C2 beaconing patterns (regular intervals)
```

## 5.3 Custom Rule Creation

```json
// Example: PowerShell encoded command detection
{
  "name": "PowerShell Encoded Command Execution",
  "type": "eql",
  "query": "process where process.name : (\"powershell.exe\", \"pwsh.exe\") and process.command_line : (\"-enc*\", \"-EncodedCommand*\", \"-en *\")",
  "severity": "high",
  "risk_score": 73,
  "tags": ["T1059.001", "Execution"]
}
```

---

# PHASE 6: SYSMON + WINLOGBEAT INTEGRATION

---

```yaml
# winlogbeat.yml optimized for Sysmon
winlogbeat.event_logs:
  - name: Microsoft-Windows-Sysmon/Operational
    event_id: 1,3,7,8,10,11,12,13,14,22

processors:
  - add_host_metadata: ~
  - add_cloud_metadata: ~

output.elasticsearch:
  hosts: ["http://elk-server:9200"]
  index: "winlogbeat-sysmon-%{+yyyy.MM.dd}"
```

- [ ] **ECS normalization of Sysmon:** Winlogbeat automatically maps Sysmon fields to ECS fields. `process.name` = Sysmon `Image`, `process.parent.name` = `ParentImage`, `network.destination.ip` = `DestinationIp`. Know these mappings.

---

# PHASE 7: PRACTICAL LABS

---

- [ ] **Lab 1 — Full Stack Deployment:** Deploy ELK (Docker Compose) + Filebeat on your Kali VM forwarding `/var/log/auth.log` to Elasticsearch. Build a Kibana dashboard showing failed SSH logins over time, top attacking IPs, and unique usernames attempted.

- [ ] **Lab 2 — Windows Telemetry:** Deploy Winlogbeat on a Windows VM (Sysmon must be running). Forward all Sysmon events to Elasticsearch. Search for Event ID 1 (Process Create) with unusual parent processes in Kibana Discover.

- [ ] **Lab 3 — Attack & Detect:** Execute an encoded PowerShell command in the Windows VM. Within 60 seconds, locate the event in Kibana Discover using KQL. Create a Detection Rule that would have alerted on it. Verify the alert fires on a second execution.

- [ ] **Lab 4 — Sigma to EQL:** Take one Sigma rule (from the SigmaHQ repository) and manually translate it to an EQL rule in Elastic Security. Test it against real log data from your lab.

---

## 📝 Operational Notes

- **Elasticsearch vs OpenSearch:** AWS forked Elasticsearch after Elastic changed its license. OpenSearch is the AWS open-source fork. Both use the same REST API and Kibana-equivalent (OpenSearch Dashboards). Know the difference if you work in AWS environments.
- **Heap sizing:** Set `ES_JAVA_OPTS` to 50% of available RAM, maximum 31GB (beyond 31GB, JVM loses compressed oops optimization and performance degrades).
- **Shard count:** For lab use, 1 shard per index is fine. For production, over-sharding kills performance. Rule of thumb: 10–50GB per shard.
- **`_source` vs `doc_values`:** `_source` stores the original JSON and enables `_reindex`. `doc_values` enables sorting and aggregations. Disabling `_source` saves disk but breaks many features — never disable it in a SIEM.
- **Elastic vs Splunk for certs:** Both vendors offer certifications. Elastic has the Elastic Certified Analyst (ECA) and Engineer (ECE). Splunk has SPLK-1002 (Core Certified User). For SOC roles, employers recognize both.
