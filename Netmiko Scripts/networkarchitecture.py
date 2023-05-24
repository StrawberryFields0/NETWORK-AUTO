from netmiko import ConnectHandler
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.252',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.251',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.250',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.249',
    'username': 'cisco',
    'password': 'cisco'
}

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.248',
    'username': 'cisco',
    'password': 'cisco'
}


with open("iosv_l2_cisco_design") as f:
    lines = f.read().splitlines()
print (lines)
    
all_devics = [iosv_l2_s4,iosv_l2_s5,iosv_l2_s6]
for devices in all_devics:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print(output)

with open('iosv_l2_core') as f:
    lines = f.read().splitlines()
print(lines)


all_devics = [iosv_l2_s2,iosv_l2_s3,iosv_l2_s4,iosv_l2_s5,iosv_l2_s6]

for devices in all_devics:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)
