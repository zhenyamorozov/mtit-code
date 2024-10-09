from ncclient import manager

conn = manager.connect(
    host='192.168.56.101',
    port=830,
    username='cisco',
    password='cisco123!'
    # hostkey_verify=False
)

for capa in conn.server_capabilities:
    print(capa)


moduleX = "Cisco-IOS-XE-cdp"
for capability in conn.server_capabilities:
    if moduleX in capability:
        print(capability + " - YANG module is supported by this router")
        