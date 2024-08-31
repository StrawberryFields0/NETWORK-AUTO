from netmiko import ConnectHandler
import getpass
IPadd1 = input("enter the IP adfdress of your switch: ")
user = input("enter your username:" )
password = getpass.getpass()

ios_l2_s1 = {
    'device_type': 'cisco_ios',
    'ip': IPadd1,
    'username': user,
    'password': password
}

with open('iosv_l2_cisco_design') as f:
    lines = f.read().splitlines()
print (lines)

all_devices = [ios_l2_s1]

for devices in all_devices:
    net_connect = ConnectHandler(**devices)
    output = net_connect.send_config_set(lines)
    print (output)