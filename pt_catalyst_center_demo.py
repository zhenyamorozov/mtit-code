import requests
import json

def get_token(username, password):
    uri = 'http://localhost:58000/api/v1/ticket'
    
    headers = {
        'Content-Type': 'application/json'
    }
    data = {
        'username': username,
        'password': password
    }
    
    resp = requests.post(uri, headers=headers, json=data)
    
    resp_json = resp.json()
    
    return resp_json['response']['serviceTicket']

def get_hosts(token):
    uri = 'http://localhost:58000/api/v1/host'
    
    headers = {
        'Accept': 'application/json',
        'X-Auth-Token': token
    }
    
    resp = requests.get(uri, headers=headers)
    
    resp_json = resp.json()
    
    return resp_json['response']

token = get_token('admin', 'admin')
print('Session token:', token)

hosts = get_hosts(token)
print(json.dumps(hosts, indent=4))