from ncclient import manager

router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

with manager.connect(host=router_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    interface_stats = m.get(filter=('subtree', '''
    <interfaces-state xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
      <interface>
        <name>GigabitEthernet1</name>
      </interface>
    </interfaces-state>
    ''')).data_xml
    print("Interface Statistics:")
    print(interface_stats)