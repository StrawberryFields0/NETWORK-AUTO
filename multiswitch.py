import getpass
import telnetlib

HOST = "localhost"
user = input("Enter your telnet username: ")
password = getpass.getpass()

f = open ("myswitches")

for IP in f:
    IP=IP.strip()
    print ("configuring switch " + IP)
    HOST = IP
    tn = telnetlib.Telnet(HOST)
    tn.read_until(b"Username: ")
    tn.write(user.encode('ascii') + b"\n")
    if password:
        tn.read_until(b"Password: ")
        tn.write(password.encode('ascii') + b"\n")
    tn.write(b"enable\n")
    tn.write(b"cisco\n")
    tn.write(b"conf t\n")
    for n in range (2,101):
        tn.write(b"vlan " + str(n).encode('ascii') + b"\n")
        tn.write(b"name Python_Vlan_" + str(n).encode('ascii') + b"\n")
    tn.write(b"end\n")
    tn.write(b"copy run start\n")
    tn.write(b" \n")
    tn.write(b"exit\n")
    print(tn.read_all().decode('ascii'))




