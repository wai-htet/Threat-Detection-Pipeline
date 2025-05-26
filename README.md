🛡️ End-to-End Threat Detection Pipeline (SIEM + SOAR Integration)

A modular, containerized cybersecurity pipeline that simulates real-time threat detection, centralized logging (SIEM), and automated incident response (SOAR). Built for scalability, automation, and real-world detection engineering.


🚀 Overview

This project demonstrates a full-stack cybersecurity pipeline using:

    Log Shippers (Filebeat)

    Ingestion & Search Engine (Elasticsearch)

    Visualization & SIEM (Kibana)

    Automation & Response (SOAR logic in Python)

    Sample Threat Simulations (e.g., failed SSH, malicious DNS queries)

It enables real-time ingestion of logs, detection of suspicious behaviors, and automated or semi-automated response actions.
📦 Architecture

[ Filebeat ] → [ Elasticsearch ] → [ Kibana (SIEM) ]
                                  ↘
                               [ SOAR (Python script or Playbook) ]

🧰 Tech Stack
Component	Tool
Log Shipper	Filebeat
SIEM Engine	Elasticsearch
Visualization	Kibana
SOAR	Custom Python
Containerization	Docker + Docker Compose
🛠️ Features

    ✅ Dockerized architecture — portable and scalable

    ✅ Real-time log ingestion from multiple sources

    ✅ Custom detection rules and dashboards in Kibana

    ✅ Automated incident response via Python-based SOAR

    ✅ Simulated attack data (failed login, DDoS, DNS tunneling)

    ✅ Easily extendable with new rules, agents, or integrations

📈 Enterprise Scalability

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
├── dashboards/              # Optional: prebuilt Kibana dashboards
└── README.md

📊 Sample Use Case

    Log failed SSH logins → Detect brute-force attempts → Trigger Python SOAR script → Block source IP using iptables or send alert via Slack/email.

💡 Future Enhancements

    ✅ Correlation engine for multi-step attack detection

    ✅ MITRE ATT&CK mapping

    ✅ REST API endpoints for external integrations

    ✅ Web UI for managing detection rules & playbooks

    ✅ Container orchestration via Kubernetes

    👨‍💻 Author

Wai Htet
Security Engineer | Cyber Threat Detection | DevSecOps
🔗 linkedin.com/in/htet-wai
https://github.com/wai-htet


📜 License

MIT License
