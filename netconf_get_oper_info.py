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

# Define the filter for operational data
netconf_filter = '''
<filter xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces"/>
</filter>
'''
# Retrieve the operational information with a standard YANG model
netconf_reply = m.get(filter=netconf_filter)

interface_oper_info = parseString(netconf_reply.xml)

print(interface_oper_info.toprettyxml())
ints = interface_oper_info.getElementsByTagName('interface')

for i in ints:
    name = i.getElementsByTagName('name')[0].firstChild.nodeValue
    phys_address = i.getElementsByTagName('phys-address')[0].firstChild.nodeValue
    stats = i.getElementsByTagName('statistics')[0]
    in_octets = stats.getElementsByTagName('in-octets')[0].firstChild.nodeValue
    out_octets = stats.getElementsByTagName('out-octets')[0].firstChild.nodeValue
    
    print(f"Name: {name} MAC: {phys_address} Input: {in_octets} Output {out_octets}")
pass
