from netmiko import ConnectHandler
from getpass import getpass

password = getpass()

ESW_1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.11',
    'username': 'puma',
    'password': password,
    'secret': password,
    'port': 22,
}

NJ_CORE_1 = {
    'device_type': 'cisco_ios',
    'ip': '192.168.122.12',
    'username': 'puma',
    'password': password,
    'secret': password,
    'port': 22,
}

for device in (ESW_1, NJ_CORE_1):
    net_connect = ConnectHandler(**device)
    output = net_connect.send_command("show arp")
    print("*" * 100)
    print(output)

for rock in (ESW_1, NJ_CORE_1):
    net_connect = ConnectHandler(**rock)
    net_connect.enable()
    output = net_connect.send_config_set(['int FastEthernet1/1', 'des UP_LINK'])
    print(output)
    print("*" * 100)
    