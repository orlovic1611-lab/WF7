# WF Framework Settings

NAME = "WF Security Framework"
VERSION = "0.2.0"

# Base paths
BASE_DIR = "/opt/wf"
DATA_DIR = f"{BASE_DIR}/data"
LOG_DIR = f"{BASE_DIR}/logs"
DB_PATH = f"{BASE_DIR}/database/wf.db"

# Dashboard configuration
DASHBOARD_HOST = "0.0.0.0"
DASHBOARD_PORT = 8080

# Plugin system
PLUGIN_DIR = f"{BASE_DIR}/plugins"
ENABLED_PLUGINS = [
    "network",
    "ports",
    "system"
]

# Reports & scans
REPORT_DIR = f"{BASE_DIR}/reports"
SCAN_DIR = f"{BASE_DIR}/scans"

# Security / debug
DEBUG = True
