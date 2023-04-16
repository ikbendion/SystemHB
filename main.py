import requests
import time
import subprocess
import yaml

# Load configuration from YAML file
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

# Access configuration variables
url = config["url"]
service = config["service"]
interval = config["interval"]

while True:
    if subprocess.run(["systemctl", "is-active", service]).returncode == 0:
        response = requests.get(url)
        print(f"OK: {service} is running")
    else:
        print(f"Error: {service} is not running")
    time.sleep(int(interval))