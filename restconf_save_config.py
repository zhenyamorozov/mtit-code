import requests
from requests.auth import HTTPBasicAuth

# Replace with your router's IP address, username, and password
router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

# The cisco-ia (Cisco Intelligent Automation) YANG model is used to facilitate
# various automation tasks on Cisco devices. The 'save-config' operation provided
# by this model allows you to save the running configuration to the startup
# configuration, ensuring that changes persist across device reboots.

# RESTCONF URL for the save-config operation
url = f"https://{router_ip}/restconf/operations/cisco-ia:save-config"

# Headers
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

# JSON payload (empty for save-config operation)
payload = {}

# Send POST request to save the running configuration to startup configuration
response = requests.post(url, headers=headers, auth=HTTPBasicAuth(username, password), json=payload, verify=False)

# Check response status
if response.status_code == 200:
    print("Configuration saved successfully.")
else:
    print(f"Failed to save configuration. Status code: {response.status_code}, Response: {response.text}")