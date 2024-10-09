import requests
from requests.auth import HTTPBasicAuth

router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=GigabitEthernet1"
headers = {
    'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

payload = {
    "ietf-interfaces:interface": {
        "name": "GigabitEthernet1",
        "description": "Updated Description",
        "type": "iana-if-type:ethernetCsmacd",
        "enabled": True
    }
}

response = requests.put(url, headers=headers, auth=HTTPBasicAuth(username, password), json=payload, verify=False)

if response.status_code == 204:
    print("Interface description updated successfully.")
else:
    print(f"Failed to update interface description. Status code: {response.status_code}, Response: {response.text}")