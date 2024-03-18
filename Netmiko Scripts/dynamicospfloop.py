from netmiko import ConnectHandler
from getpass import getpass 
# importing needed dependencies
def get_network_from_user(network_num: int) -> str:
    network = input(f"Network {network_num} that you want to broadcast for OSPF: ")
    wild_card_mask = input(f"Network {network_num} put in the wildcard mask for your network: ")
    area = input(f"Network {network_num} put in the area for OSPF: ")
    return "network " + network + " " + wild_card_mask + " area " + area

def main():
  ip_address = input("enter the IP address of your router: ")
  user = input("enter your username: ")
  password = getpass(prompt="enter your password: ")
  ios_l3_r1 = {
      'device_type': 'cisco_ios',
      'ip': ip_address,
      'username': user,
      'password': password,
  }
  
  router_id = input("put in your desired router ID: ")
  
  # get an integer from the user
  not_int = True
  loop_counter = 0
  while not_int:
      loop_counter = input("how many networks do you want to define? ")
      try:
          loop_counter = int(loop_counter)
          not_int = False
      except:
          print("that is not an integer dumbass, try again")
  
  networks = []
  for num in range(loop_counter):
      networks.append(get_network_from_user(num + 1))
  
  # dynamic definitions for inputs for ospf
  ospf_commands = ["router ospf " + router_id]
  for network in networks:
      ospf_commands.append(network)
  
  print(ospf_commands)
  print()
  input("continue?")
  # Defining the OSPF commands to be used
  net_connect = ConnectHandler(**ios_l3_r1)
  output = net_connect.send_command('show ip route')
  # Connecting to the router and having it show routes
  output += net_connect.send_config_set(ospf_commands)
  net_connect.save_config()
  output += net_connect.send_command('show ip route')
  print(output)
  
if __name__ == "__main__":
    main()

# Thank you Odyhibit for help in this one

