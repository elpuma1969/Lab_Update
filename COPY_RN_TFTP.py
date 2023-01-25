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


def tftp_cp_run():
    with open('devices_file.txt') as f:
        devices_list = f.read().splitlines()

    for devices in devices_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': user_1,
            'password': password_1,
        }

        command = "copy running-config tftp:"
        command2 = '192.168.122.126'

        start_time = datetime.now()

        net_connect = ConnectHandler(**ios_device)

        output = net_connect.send_command_timing(command, strip_prompt=False, strip_command=False, delay_factor=4)

        output2 = net_connect.send_command_timing(command2, strip_prompt=False, strip_command=False, delay_factor=4)

        if "Address or name of remote host" in output:
            print("Starting copy...")
            output += net_connect.send_command("\n", delay_factor=4, expect_string=r"#")
            output2 += net_connect.send_command("\n", delay_factor=4, expect_string=r"#")
        net_connect.disconnect()

        if "Destination filename" in output:
            print("Starting copy...")
            output += net_connect.send_command("\n", delay_factor=4, expect_string=r"#")
        net_connect.disconnect()

    end_time = datetime.now()
    print(f"\n{output}\n")
    print(f'\n{output2}\n')
    print("done")
    print(f"Execution time: {start_time - end_time}")


tftp_cp_run()
