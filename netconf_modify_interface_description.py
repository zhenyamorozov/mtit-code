from ncclient import manager

router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

config_payload = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <native xmlns="http://cisco.com/ns/yang/Cisco-IOS-XE-native">
    <router>
      <ospf>
        <id>1</id>
        <router-id>1.1.1.1</router-id>
        <network>
          <ip>192.168.1.0</ip>
          <mask>0.0.0.255</mask>
          <area>0</area>
        </network>
      </ospf>
    </router>
  </native>
</config>
"""

with manager.connect(host=router_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    m.edit_config(target='running', config=config_payload)
    print("OSPF configuration applied successfully.")