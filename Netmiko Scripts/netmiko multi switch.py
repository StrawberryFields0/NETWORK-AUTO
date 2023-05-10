from netmiko import ConnectHandler

iosv_l2_s6 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.248',
    'username': 'cisco',
    'password': 'cisco'
}
iosv_l2_s5 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.249',
    'username': 'cisco',
    'password': 'cisco'
}
iosv_l2_s4 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.250',
    'username': 'cisco',
    'password': 'cisco'
}
iosv_l2_s3 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.251',
    'username': 'cisco',
    'password': 'cisco'
}
iosv_l2_s2 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.252',
    'username': 'cisco',
    'password': 'cisco'
}
iosv_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.253',
    'username': 'cisco',
    'password': 'cisco'
}
all_devices = [iosv_l2_s6,iosv_l2_s5, iosv_l2_s4,iosv_l2_s3,iosv_l2_s2,iosv_l2_s1 ]
for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    for n in range (2,101):
        print ("Creating VLAN " + str(n))
        config_commands = ['vlan ' + str(n), 'name Python_VLAN ' + str(n)]
        output = net_connect.send_config_set(config_commands)
        print (output) 
    config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
    output = net_connect.send_config_set(config_commands)
    print(output)
    net_connect.disconnect()