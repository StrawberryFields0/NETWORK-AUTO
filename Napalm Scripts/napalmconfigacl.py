
import json
from napalm import get_network_driver
driver = get_network_driver('ios')
iosvl3switch = {
        'hostname': '192.168.122.254',
        'username': 'cisco',
        'password': 'cisco',
         "optional_args": {"secret": 'cisco'}
        }


iosvl3switch_conn = driver(**iosvl3switch)
iosvl3switch_conn.open()
print(f"Connecting to {iosvl3switch['hostname']}")
iosvl3switch_conn.load_merge_candidate(filename='ACL1.cfg')
iosvl3switch_conn.commit_config()
iosvl3switch_conn.close()
