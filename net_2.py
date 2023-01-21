from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

my_device = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.11',
    'username': 'puma',
    'password': password,
    'secret': password,
    'port': 22,
}


net_connect = ConnectHandler(**my_device)
output = net_connect.send_command('show ip int brief')
print(output)
print('*' * 100)
net_connect.enable()
output1 = net_connect.send_config_set(['int FastEthernet0/1', 'no shutdown'])
print(output1)


