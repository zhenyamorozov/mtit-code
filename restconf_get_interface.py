import requests
import json

url = 'https://192.168.56.101/restconf/data/ietf-interfaces:interfaces'

headers = {
    # 'Content-Type': 'application/yang-data+json',
    'Accept': 'application/yang-data+json'
}

auth = ('cisco', 'cisco123!')   # tuple - immutable

resp = requests.get(url, headers=headers, auth=auth, verify=False)

print(resp.status_code)
resp_data = resp.json()
print(json.dumps(resp_data, indent=4))
print(json.loads(resp.text))


