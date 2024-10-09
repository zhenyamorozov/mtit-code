from ncclient import manager
from ncclient.xml_ import to_ele

router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

# Correct payload for reloading the device
reboot_payload = """
<rpc message-id="101" xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <reload xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-rpc">
        <reason>Reboot via NETCONF</reason>
    </reload>
</rpc>
"""

try:
    with manager.connect(host=router_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
        # Send the reboot command
        response = m.dispatch(to_ele(reboot_payload))
        print("System reboot initiated successfully.")
        print(response)

except Exception as e:
    print(f"Failed to connect to the device: {e}")