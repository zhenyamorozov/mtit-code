import requests
import json

url = 'https://192.168.56.101/restconf/data/ietf-interfaces:interfaces/interface=Loopback99'

headers = {
    "Accept": "application/yang-data+json",
    'Content-Type': 'application/yang-data+json'
}

auth = ('cisco', 'cisco123!')   # tuple - immutable

payload = {
    'ietf-interfaces:interface':
        {
            'name': 'Loopback99', 
            'description': 'My Loopback interface', 
            'enabled': True, 
            'type': 'iana-if-type:softwareLoopback',
            'ietf-ip:ipv4': {
                'address': [
                    {
                        'ip': '1.1.1.1',
                        'netmask': '255.255.255.0'
                    },
                    {
                        'ip': '2.2.2.1',
                        'netmask': '255.255.255.0'
                    }

                ]
            }, 
            'ietf-ip:ipv6': {}
        }
}

resp = requests.put(    # change to DELETE
    url, 
    headers=headers, 
    auth=auth, 
    json=payload,    # remove payload
    verify=False
)

print(resp.status_code)
# resp_data = resp.json()
# print(json.dumps(resp_data, indent=4))
pass


