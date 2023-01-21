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
    print("Entering enable mode")
    output = net_connect.send_config_from_file('commands_file.txt')

    prompt = net_connect.find_prompt()
    hostname = prompt[0:-1]

    from datetime import datetime

    now = datetime.now()
    year = now.year
    month = now.month
    day = now.day

    filename = f"{hostname}_{year}_{month}_{day}._Update.txt"

    with open(filename, "w") as f:
        f.write(output)
        print(f"Backup of {hostname} completed successfully")
        print("#" * 80)

    print("Closing connection to device")
    net_connect.disconnect()

