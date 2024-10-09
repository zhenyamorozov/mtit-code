import requests
from requests.auth import HTTPBasicAuth

router_ip = '192.168.1.1'
username = 'your_username'
password = 'your_password'

url = f"https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface=Loopback0"
headers = {'Accept': 'application/yang-data+json'}

response = requests.delete(url, headers=headers, auth=HTTPBasicAuth(username, password), verify=False)

if response.status_code == 204:
    print("Loopback interface deleted successfully.")
else:
    print(f"Failed to delete loopback interface. Status code: {response.status_code}, Response: {response.text}")