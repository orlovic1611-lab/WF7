# WF7.2 Security Framework

WF7.2 je stabilná verzia moderného bezpečnostného frameworku pre Linux systémy.
Obsahuje runtime, PRO engine, cloud API, enterprise agenta, modulárnu architektúru
a plnú CLI podporu.

## 🚀 Features
- Real-time sensors
- AI anomaly detection (PRO)
- Enterprise agent (systemd)
- Cloud API (Flask, port 7070)
- Modular plugin architecture
- Score engine, threat engine, watchdog
- PRO dashboard (web)
- Zero-config installation

## 📦 Installation
apt install ./wf7_fixed.deb
systemctl enable wf7-agent
systemctl start wf7-agent

## 🖥 CLI Usage
wf --help
wf plugins
wf super

## 🌐 API Endpoints
- /api/status
- /api/modules

## 📁 Components
- Runtime: /opt/wf7/wf.py
- PRO Engine: /opt/wf7/pro_engine/
- Cloud API: /opt/wf7/cloud_api/
- Enterprise Agent: /opt/wf7/wf7_agent.py
- Systemd Service: /usr/lib/systemd/system/wf7-agent.service

## 📄 Version
WF7.2 – Stable Release
