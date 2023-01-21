from netmiko import ConnectHandler
from getpass import getpass

net_connect = ConnectHandler(device_type='cisco_ios', ip='192.168.122.11', username='puma', password=getpass())

print(net_connect.find_prompt())
net_connect.disconnect()





