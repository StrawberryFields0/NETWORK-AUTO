import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl2_1 = {
        'hostname': '192.168.122.253',
        'username': 'cisco',
        'password': 'cisco',
         "optional_args": {"secret": 'cisco'}
        }
iosvl2_1_conn = driver(**iosvl2_1)
iosvl2_1_conn.open()
print(f"Connecting to {iosvl2_1['hostname']}")
ios_output = iosvl2_1_conn.get_facts()
print (json.dumps(ios_output, indent=4))
ios_output = iosvl2_1_conn.get_interfaces()
print (json.dumps(ios_output, indent=4))
ios_output = iosvl2_1_conn.get_interfaces_counters()
print (json.dumps(ios_output, indent=4))


