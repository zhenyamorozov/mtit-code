import requests
import json
from requests.auth import HTTPBasicAuth

# Replace with your router's IP address, username, and password
router_ip = 'router_ip_address'
username = 'your_username'
password = 'your_password'

# RESTCONF URL for the interface
url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=Loopback0"

# Headers
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

# JSON payload to create a new Loopback interface
payload = {
    "ietf-interfaces:interface": {
        "name": "Loopback0",
        "description": "Test Loopback Interface",
        "type": "iana-if-type:softwareLoopback",
        "enabled": True,
        "ietf-ip:ipv4": {
            "address": [
                {
                    "ip": "192.0.2.1",
                    "netmask": "255.255.255.0"
                }
            ]
        }
    }
}

# Add the interface
response = requests.put(url, headers=headers, auth=HTTPBasicAuth(username, password), data=json.dumps(payload), verify=False)
if response.status_code == 201 or response.status_code == 204:
    print("Interface added successfully.")
else:
    print(f"Failed to add interface. Status code: {response.status_code}, Response: {response.text}")

# Verify the interface configuration
response = requests.get(url, headers={'Accept': 'application/yang-data+json'}, auth=HTTPBasicAuth(username, password), verify=False)
if response.status_code == 200:
    print("Interface configuration:")
    print(json.dumps(response.json(), indent=2))
else:
    print(f"Failed to retrieve interface configuration. Status code: {response.status_code}, Response: {response.text}")

