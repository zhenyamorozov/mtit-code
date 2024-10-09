import requests
from requests.auth import HTTPBasicAuth

router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces-state/interface=GigabitEthernet1"
headers = {'Accept': 'application/yang-data+json'}

response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)

if response.status_code == 200:
    print("Interface statistics:")
    print(response.json())
else:
    print(f"Failed to retrieve interface statistics. Status code: {response.status_code}, Response: {response.text}")