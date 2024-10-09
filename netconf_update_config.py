from ncclient import manager
from xml.dom.minidom import parseString
# from ncclient.operations.rpc import RPCError

# Create the NETCONF connection manager object
m = manager.connect(
    host='192.168.56.101',
    port=830,
    username='cisco',
    password='cisco123!'
    # hostkey_verify=False
)

# Change the device hostname
new_hostname = 'MyCoolBox'
config_data = f'''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <hostname>{new_hostname}</hostname>
    </native>
</config>
'''

netconf_reply = m.edit_config(target='running', config=config_data)
print(netconf_reply)


# Configure a loopback interface
config_data = f'''
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <interface>
            <Loopback>
                <name>112</name>
                <description>This interface is created via NETCONF!</description>
                <ip>
                    <address>
                        <primary>
                            <address>111.111.111.112</address>
                            <mask>255.255.255.0</mask>
                        </primary>
                    </address>
                </ip>
            </Loopback>
        </interface>
    </native>
</config>
'''

# Handle exceptions raised in the NETCONF operation
try:
    netconf_reply = m.edit_config(target='running', config=config_data)
    print(netconf_reply)
except Exception as ex:
    print('Something went wrong')
    print(ex)
    print(ex.info)
    
# Change ncclient manager exception raise mode
m.raise_mode = 0
# Call NETCONF function with exceptions suppressed
netconf_reply = m.edit_config(target='running', config=config_data)
print(netconf_reply)

print('End of the program')