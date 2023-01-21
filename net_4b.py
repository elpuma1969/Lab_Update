from netmiko import ConnectHandler
from getpass import getpass

user_1 = input("Enter your username: ")
password_1 = getpass()


class MyNetmiko:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

    def connect(self):
        connection = ConnectHandler(device_type=self.device_type, host=self.host, username=self.username,
                                    password=self.password)
        return connection


with open('commands_file.txt') as f:
    commands_list = f.read().splitlines()

with open('devices_file.txt') as f:
    devices_list = f.read().splitlines()

for devices in devices_list:
    print('Connecting to device" ' + devices)
    ip_address_of_device = devices
    ios_device = {
        'device_type': 'cisco_ios',
        'ip': ip_address_of_device,
        'username': user_1,
        'password': password_1
    }

    net_connect = ConnectHandler(**ios_device)

    output = net_connect.send_config_from_file('commands_file.txt')
    print(output)
