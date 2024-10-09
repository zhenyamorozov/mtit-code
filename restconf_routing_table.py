import requests
from requests.auth import HTTPBasicAuth

router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

url = f"https://{router_ip}/restconf/data/ietf-routing:routing-state"
headers = {'Accept': 'application/yang-data+json'}

response = requests.get(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)

if response.status_code == 200:
    print("Routing table:")
    print(response.json())
else:
    print(f"Failed to retrieve routing table. Status code: {response.status_code}, Response: {response.text}")