import requests
from requests.auth import HTTPBasicAuth

# Replace with your router's IP address, username, and password
router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

# RESTCONF URL for the reload operation
# url = f"https://{router_ip}/restconf/operations/cisco-ia:reload"
# url = f"https://{router_ip}/restconf/data/netconf-state/capabilities"
url = f"https://{router_ip}/restconf/operations/ietf-system:reboot"

# Headers
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

# JSON payload (empty for reload operation)
payload = {}

# Send POST request to reboot the router
response = requests.post(url, headers=headers, auth=HTTPBasicAuth(username, password), json=payload, verify=False)

# Check response status
if response.status_code == 200:
    print("Router reboot initiated successfully.")
else:
    print(f"Failed to initiate router reboot. Status code: {response.status_code}, Response: {response.text}")