import json
from napalm import get_network_driver

bgplist = ['192.168.122.254',
           '192.168.122.253']
driver = get_network_driver('ios')
iosvrouter = {
        'hostname': '192.168.122.254',
        'username': 'cisco',
        'password': 'cisco',
         "optional_args": {"secret": 'cisco'}
        }
iosvl3switch = {
        'hostname': '192.168.122.254',
        'username': 'cisco',
        'password': 'cisco',
         "optional_args": {"secret": 'cisco'}
        }
all_devices = [iosvrouter,iosvl3switch]
for devices in all_devices:
    devices_conn = driver(**devices)
    devices_conn.open()
    print(f"Connecting to {devices['hostname']}")
    bgp_neighbors = devices_conn.get_bgp_neighbors()
    devices_conn.close()
    print (json.dumps(bgp_neighbors, indent=4))