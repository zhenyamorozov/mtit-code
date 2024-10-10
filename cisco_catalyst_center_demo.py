import requests
import json

def get_token(username, password):
    uri = 'https://sandboxdnac.cisco.com/dna/system/api/v1/auth/token'
    
    headers = {
        'Content-Type': 'application/json'
    }
    
    auth = (username, password)
    
    resp = requests.post(uri, headers=headers, auth=auth, verify=False)
    
    if resp.status_code != 200:
        return None
    else:
        resp_json = resp.json()
        return resp_json['Token']


def list_devices(token):
    uri = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device'
    
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': token
    }
    
    resp = requests.get(uri, headers=headers, verify=False)
    
    if resp.status_code != 200:
        return None
    else:
        resp_json = resp.json()
        return resp_json['response']


def run_commands(token, commands, deviceIds):
    uri = 'https://sandboxdnac.cisco.com/dna/intent/api/v1/network-device-poller/cli/read-request'
    
    headers = {
        'Content-Type': 'application/json',
        'Accept': 'application/json',
        'X-Auth-Token': token
    }
    
    data = {
        'commands': commands,
        'deviceUuids': deviceIds
    }
    
    resp = requests.post(uri, headers=headers, json=data, verify=False)
    
    resp_json = resp.json()
    
    return resp_json['response']['taskId']

def get_task(token, taskId):
    uri = f'https://sandboxdnac.cisco.com/dna/intent/api/v1/task/{taskId}'
    
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': token
    }
    
    resp = requests.get(uri, headers=headers, verify=False)
    
    resp_json = resp.json()
    # print(json.dumps(resp_json, indent=4))
    return resp_json['response']

def get_file(token, fileId):
    uri = f'https://sandboxdnac.cisco.com/dna/intent/api/v1/file/{fileId}'

    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': token
    }
    
    resp = requests.get(uri, headers=headers, verify=False)
    
    resp_json = resp.json()
    
    return resp_json
    

# Authenticate and obtain the token
token = get_token('devnetuser', 'Cisco123!')
print(token)

# Retrieve the list of network devices
devices = list_devices(token)
print(json.dumps(devices, indent=4))

# Extract device IDs and populate the list of device IDs
device_ids = []
for d in devices:
    device_ids.append(d['id'])

my_commands = ['show version', 'show running-config', 'show ip route', 'show process', 'show startup']

task_id = run_commands(token, my_commands, device_ids)
print('The task has started:', task_id)

task = get_task(token, task_id)

file_id = json.loads(task['progress'])['fileId']

output = get_file(token, file_id)

for d in output:
    for c in d['commandResponses']['SUCCESS']:
        print('Device:', d['deviceUuid'])
        print(d['commandResponses']['SUCCESS'][c])
        print('Press Enter to continue...')
        print()
        input()
