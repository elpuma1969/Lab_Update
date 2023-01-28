from netmiko import ConnectHandler
import schedule
import time
from datetime import datetime


class MyNetmiko:
    def __init__(self, device_type, host, username, password, read_timeout=300):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password
        self.read_timeout = read_timeout

    def connect(self):
        net_con = ConnectHandler(device_type=self.device_type, host=self.host, username=self.username,
                                 password=self.password)
        return net_con


def backup_2_file():
    username = 'puma'
    password = "cisco"

    with open('comm1.txt') as f:
        commands_list = f.read().splitlines()

    with open('avi_device.txt') as f:
        devices_list = f.read().splitlines()

    for devices in devices_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': username,
            'password': password,
            'secret': password,
            'port': 22,

        }
        connection = ConnectHandler(**ios_device)
        print('Entering the enable mode...')
        connection.enable()

        output = connection.send_config_from_file(""/home/puma/Desktop/pthon_gig/configs_switches/"
                                                  "description_commands.txt"")
        print(output)

        prompt = connection.find_prompt()
        hostname = prompt[0:-1]

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        filename = '/home/puma/Desktop/pthon_gig/BACKUPS/' + f'{hostname}_{year}-{month}-{day}_com_test.txt'

        with open(filename, 'w') as final:
            final.write(output)
            print(f'Backup of {hostname} completed successfully')
            print('#' * 30)

        print('Closing connection')
        connection.disconnect()


backup_2_file()


def save_commands():
    username = 'puma'
    password = "cisco"

    # with open('comm1.txt') as f:
    #     commands_list = f.read().splitlines()

    with open('avi_device.txt') as f:
        devices_list = f.read().splitlines()

    for devices in devices_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': username,
            'password': password,
            'secret': password,
            'port': 22,

        }
        connection = ConnectHandler(**ios_device)
        print('Entering the enable mode...')
        connection.enable()
        output = connection.send_command("show run")
        output += connection.send_command("write memory")
        print(output)

        prompt = connection.find_prompt()
        hostname = prompt[0:-1]

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        filename = '/home/puma/Desktop/pthon_gig/BACKUPS/' + f'{hostname}_{year}-{month}-{day}_after_config.txt'

        with open(filename, 'w') as final:
            final.write(output)
            print(f'Backup of {hostname} completed successfully')
            print('#' * 50)

        print('Closing connection')
        connection.disconnect()


save_commands()




