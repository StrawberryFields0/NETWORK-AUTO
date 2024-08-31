from netmiko import ConnectHandler
import getpass
# Importing required dependinceis for the script
def IPadd1 = input("enter the IP adfdress of your router: ")
# Defining the Ipaddress for your device your configuring 
def user = input("enter your username:" )
# Dynamicly defining your username 
def password = getpass.getpass()
# Dynamically defining your password
ios_l3_R1 = {
    'device_type': 'cisco_ios',
    'ip': IPadd1,
    'username': user,
    'password': password,
}
# Dictionary for Netmiko connection 
network1 = input("put in your network that you want to broadcast for OSPF:")
wildcardmask1 = input("put in the wildcard mask for your network:")
area1 = input("put in the area for OSPF")
routerid1 = input("put in your desired router ID")
network2 = input("put in your network that you want to broadcast for OSPF:")
wildcardmask2 = input("put in the wildcard mask for your network:")
area2 = input("put in the area for OSPF")
# dynamic definitions for inputs for ospf
ospf_commands = [
    "router ospf " + routerid1,
    "network " + network1 + " " + wildcardmask1 + " " + area1,
    "network " + network2 + " " + wildcardmask2 + " " + area2
]
# Defining the OSPF commands to be used
net_connect = ConnectHandler(**ios_l3_R1)
output = net_connect.send_command('show ip route')
# Connecting to the router and having it show routes 
output = net_connect.send_config_set(ospf_commands)
net_connect.save_config() 
output = net_connect.send_command('show ip route')
print(output)