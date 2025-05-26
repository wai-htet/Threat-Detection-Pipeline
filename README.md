# 🚨 End-to-End Threat Detection Pipeline (SIEM + SOAR Integration)

This project simulates a real-world **enterprise-grade security monitoring and response pipeline** using open-source tools. It combines **SIEM (Kibana + Elasticsearch + Filebeat)** and a **custom SOAR automation script** to detect and respond to security threats.

---

## 🧠 Project Highlights

- **Log Ingestion** via Filebeat from system logs and dummy datasets
- **Centralized Search and Analysis** with Elasticsearch
- **Interactive Dashboards & Detection Rules** via Kibana
- **Custom Python-based SOAR** for automated blocking and alerting
- **Realistic Simulation** of SSH brute force, data exfiltration, geolocation anomalies, and more

---
It enables real-time ingestion of logs, detection of suspicious behaviors, and automated or semi-automated response actions.
📦 Architecture

[ Filebeat ] → [ Elasticsearch ] → [ Kibana (SIEM) ]
                                  ↘
                               [ SOAR (Python script or Playbook) ]

## 📊 Dashboards Built (Kibana)

1. **Abnormal Login Times**
   - Simulates logins outside working hours using ecommerce timestamps
   - Visualizes anomalies grouped by user role (e.g. gender as metaphor)

2. **Suspicious User Behavior**
   - Detects repeated access to same resources (simulating brute force or enumeration)

3. **Geolocation Mapping**
   - Shows login attempts from unexpected global regions

4. **High-Value Activity (Data Exfiltration)**
   - Tracks access to "sensitive" items (mapped from product data)

📷 Screenshots available in the `screenshots/` folder.


🧰 Tech Stack

- **Filebeat** – log shipper
- **Elasticsearch** – search & storage
- **Kibana** – dashboards and detection rules
- **Python (SOAR script)** – incident response automation
- **Docker** – container orchestration for quick setup

## 🔁 Automation Script

A Python script automates incident response:
- Blocks suspicious IPs using `iptables`
- Logs incidents to CSV
- Sends Slack notifications

```python
def respond_to_alert(ip):
    block_ip(ip)
    log_incident(ip)
    notify(ip)


 🔭 Enterprise Scalability

    Deploy with Kubernetes

    Integrate with tools like TheHive, MISP, or Shuffle

    Extend to cloud-native logging via Beats agents

    Map alerts to MITRE ATT&CK

This proof-of-concept can be scaled into an enterprise-grade solution by:

    Multi-node Elasticsearch cluster for high availability

    Load balancing Filebeat agents across endpoints

    Integration with production-grade SOAR platforms like TheHive, Shuffle, Cortex XSOAR

    Use of SIEM pipelines (Logstash, Kafka) for large-scale ingestion

    Custom detection engineering using Elastic Common Schema (ECS)

    Alert enrichment and correlation with threat intelligence feeds

    Authentication and RBAC for Kibana and Elasticsearch

    Cloud-native deployment with Kubernetes and persistent storage

⚙️ Setup Instructions

# Clone the repo
git clone https://github.com/your-username/Threat-Detection-Pipeline.git
cd Threat-Detection-Pipeline

# Start all containers
docker-compose up -d

# Access Kibana (default):
http://localhost:5601

📂 Directory Structure

Threat-Detection-Pipeline/
│
├── docker-compose.yml       # Core container orchestration
├── filebeat/
│   └── filebeat.yml         # Log shipper configuration
├── soar/
│   └── responder.py         # SOAR automation logic
├── logs/                    # Sample logs for ingestion
├── dashboards/              # Kibana dashboards
└── README.md

📊 Sample Use Case

    Log failed SSH logins → Detect brute-force attempts → Trigger Python SOAR script → Block source IP using iptables or send alert via Slack/email.

💡 Future Enhancements

    ✅ Correlation engine for multi-step attack detection

    ✅ MITRE ATT&CK mapping

    ✅ REST API endpoints for external integrations

    ✅ Web UI for managing detection rules & playbooks

    ✅ Container orchestration via Kubernetes

📎 References

    Elastic SIEM Docs
    MITRE ATT&CK
    SOAR Open Source


 👨‍💻 Author
Wai Htet
Security Engineer | Cyber Threat Detection | DevSecOps
🔗 linkedin.com/in/htet-wai
https://github.com/wai-htet


📜 License

MIT License
