from ncclient import manager

router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

with manager.connect(host=router_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    for capability in m.server_capabilities:
        print(capability)