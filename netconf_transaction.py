# The `candidate` datastore is disabled by default on CSR1000v.
# Enable:
# configure terminal
# netconf-yang
# netconf-yang feature candidate-datastore
# end
# write memory

from ncclient import manager
from ncclient.xml_ import to_ele

# Replace with your router's IP address, username, and password
router_ip = '192.168.56.101'
username = 'cisco'
password = 'cisco123!'

# Example configuration payloads with the same IP address for both interfaces
config_payload1 = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback1</name>
      <description>Loopback Interface 1</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>192.168.1.1</ip>
          <netmask>255.255.255.0</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""

config_payload2 = """
<config xmlns="urn:ietf:params:xml:ns:netconf:base:1.0">
  <interfaces xmlns="urn:ietf:params:xml:ns:yang:ietf-interfaces">
    <interface>
      <name>Loopback2</name>
      <description>Loopback Interface 2</description>
      <type xmlns:ianaift="urn:ietf:params:xml:ns:yang:iana-if-type">ianaift:softwareLoopback</type>
      <enabled>true</enabled>
      <ipv4 xmlns="urn:ietf:params:xml:ns:yang:ietf-ip">
        <address>
          <ip>192.168.1.1</ip>
          <netmask>255.255.255.0</netmask>
        </address>
      </ipv4>
    </interface>
  </interfaces>
</config>
"""



# Connect to the router using NETCONF
with manager.connect(host=router_ip, port=830, username=username, password=password, hostkey_verify=False) as m:
    try:
        # Lock the candidate configuration
        m.lock(target='candidate')

        # Edit the candidate configuration
        print("Editing candidate configuration...")
        m.edit_config(target='candidate', config=config_payload1)
        m.edit_config(target='candidate', config=config_payload2)

        # Commit the candidate configuration
        print("Committing configuration changes...")
        m.commit()

        print("Configuration changes committed successfully.")

    except Exception as e:
        # Discard changes if any error occurs
        m.discard_changes()
        print(f"Failed to commit configuration changes: {e}")

    finally:
        # Unlock the candidate configuration
        m.unlock(target='candidate')
