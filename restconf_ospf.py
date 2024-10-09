import requests
import json

router1_ip = '192.168.56.101'
router2_ip = '192.168.56.102'
username = 'cisco'
password = 'cisco123!'

requests.packages.urllib3.disable_warnings()


def configure_interface(router_ip, interface_name, ip_address, subnet_mask):
    url = f'https://{router_ip}/restconf/data/ietf-interfaces:interfaces/interface={interface_name}'
    headers = {
        'Content-Type': 'application/yang-data+json'
    }
    auth = (username, password)
    data = {
        'ietf-interfaces:interface': {
            'name': interface_name, 
            'description': f'Interface {interface_name}', 
            'enabled': True, 
            'type': 'iana-if-type:softwareLoopback',
            'ietf-ip:ipv4': {
                'address': [
                    {
                        'ip': ip_address,
                        'netmask': subnet_mask
                    }
                ]
            }
        }
    }

    resp = requests.put(
        url,
        headers=headers,
        auth=auth,
        json=data,
        verify=False
    )
    print('Configured interface', interface_name, resp.status_code)
    return resp.status_code




def configure_ospf(router_ip, router_id, networks):
    ''' networks as a list of dicts:
        'ip',
        'wildcard',
        'area'
    '''
    url = f'https://{router_ip}/restconf/data/Cisco-IOS-XE-native:native/router'
    headers = {
        'Content-Type': 'application/yang-data+json'
    }
    auth = (username, password)
    data = {
        'Cisco-IOS-XE-native:router': {
            'Cisco-IOS-XE-ospf:router-ospf': {
                'ospf': {
                    'process-id': [
                        {
                            'id': 1,
                            'router-id': router_id,
                            'network': networks
                        }
                    ]
                }
            }
        }
    }
    resp = requests.put(
        url,
        headers=headers,
        auth=auth,
        json=data,
        verify=False
    )
    print('Configured OSPF router ID', router_id, resp.status_code)
    return resp.status_code




# Configure R1 interfaces
configure_interface('192.168.56.101', 'Loopback100', '192.168.100.1', '255.255.255.0')
configure_interface('192.168.56.101', 'Loopback101', '192.168.101.1', '255.255.255.0')
configure_interface('192.168.56.101', 'Loopback102', '192.168.102.1', '255.255.255.0')
configure_interface('192.168.56.101', 'Loopback103', '192.168.103.1', '255.255.255.0')

# Configure R1 OSPF process and networks
nets = [
    {
        'ip': '192.168.56.0',
        'wildcard': '0.0.0.255',
        'area': 0
    },
    {
        'ip': '192.168.100.0',
        'wildcard': '0.0.0.255',
        'area': 0
    },
    {
        'ip': '192.168.101.0',
        'wildcard': '0.0.0.255',
        'area': 0
    },
    {
        'ip': '192.168.102.0',
        'wildcard': '0.0.0.255',
        'area': 0
    },
    {
        'ip': '192.168.103.0',
        'wildcard': '0.0.0.255',
        'area': 0
    }
]
configure_ospf('192.168.56.101', '0.0.0.1', nets)


# Configure R2 interfaces
configure_interface('192.168.56.102', 'Loopback0', '10.0.0.1', '255.255.255.224')
configure_interface('192.168.56.102', 'Loopback1', '10.0.0.33', '255.255.255.224')
configure_interface('192.168.56.102', 'Loopback2', '10.0.0.65', '255.255.255.224')
configure_interface('192.168.56.102', 'Loopback3', '10.0.0.97', '255.255.255.224')

# Configure R2 OSPF process and networks
nets = [
    {
        'ip': '192.168.56.0',
        'wildcard': '0.0.0.255',
        'area': 0
    },
    {
        'ip': '10.0.0.0',
        'wildcard': '0.0.0.31',
        'area': 0
    },
    {
        'ip': '10.0.0.32',
        'wildcard': '0.0.0.31',
        'area': 0
    },
    {
        'ip': '10.0.0.64',
        'wildcard': '0.0.0.31',
        'area': 0
    },
    {
        'ip': '10.0.0.96',
        'wildcard': '0.0.0.31',
        'area': 0
    }
]
configure_ospf('192.168.56.102', '0.0.0.2', nets)

