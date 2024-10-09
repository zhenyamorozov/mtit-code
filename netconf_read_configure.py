from ncclient import manager
from xml.dom.minidom import parseString

# Create the NETCONF connection manager object
m = manager.connect(
    host='192.168.56.101',
    port=830,
    username='cisco',
    password='cisco123!'
    # hostkey_verify=False
)


# Retrieve the full configuration from the running data store
netconf_reply = m.get_config(source='running')
# print(netconf_reply)

# Beautify it and print
running_conf = parseString(netconf_reply.xml).toprettyxml()
# print(running_conf)

# Define the filter for configuration
netconf_filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
    <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
        <line>
            <console/>
        </line>
        <hostname/>
    </native>
</filter>
'''
# Retrieve the part of the config
netconf_reply = m.get_config(source='running', filter=netconf_filter)

running_conf = parseString(netconf_reply.xml).toprettyxml()
print(running_conf)

pass

def func(a):
    '''This function does nothing'''
    
    st1 = 'This is a string'
    st2 = 'This is line 1\nThis is line 2'
    st3 = '''
    This is line 1
    This is line 2
    This is line 3
    '''
    pass