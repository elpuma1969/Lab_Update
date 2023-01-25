from netmiko import ConnectHandler
from getpass import getpass
from datetime import datetime

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


def tftp_flash_1():

    with open("devices_file.txt") as f:
        devices_list = f.read().splitlines()

    for devices in devices_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': user_1,
            'password': password_1,
            'port': 22,
        }

        ssh = ConnectHandler(**ios_device)
        print('Entering the enable mode...')
        ssh.enable()

        command = "copy tftp://10.216.2.187/isr4200_4300_rommon_1612_2r_SPA.pkg " \
                  "flash:/isr4200_4300_rommon_1612_2r_SPA.pkg"

        start_time = datetime.now()

        net_connect = ConnectHandler(**ios_device)

        output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False, delay_factor=4)

        if "Destination filename" in output:
            print("Starting copy...")
            output += net_connect.send_command("\n", delay_factor=4, read_timeout=500, expect_string=r"#")
        net_connect.disconnect()

        end_time = datetime.now()
        print(f"\n{output}\n")
        print("done")
        print(f"Execution time: {start_time - end_time}")


tftp_flash_1()