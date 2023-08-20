from netmiko import ConnectHandler
import getpass
IPadd1 = input("enter the IP adfdress of your switch: ")
user = input("enter your username:" )
password = getpass.getpass()
iosv_l2 = {
   'device_type': 'cisco_ios',
    'ip': IPadd1,
    'username': user,
    'password': password
}

net_connect = ConnectHandler(**iosv_l2)
output = net_connect.send_command('show ip int brief')
print (output)

config_commands = ['int loop 0', 'ip address 1.1.1.1 255.255.255.0']
output = net_connect.send_config_set(config_commands)
print (output)