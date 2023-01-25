from netmiko import ConnectHandler


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


def send_com():

    with open('commands_file.txt') as f:
        commands_list = f.read().splitlines()

    with open('devices_file.txt') as f:
        device_list = f.read().splitlines()

    # Usage
    for devices in device_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': 'puma',
            'password': 'cisco',
            'port': 22,
        }

        net_con = ConnectHandler(**ios_device)
        print("Entering enable mode")
        net_con.enable()

        output = net_con.send_config_set(commands_list)

        prompt = net_con.find_prompt()
        hostname = prompt[0:-1]

        from datetime import datetime

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        filename = f'{hostname}_{year}-{month}-{day}_TesT.txt'

        with open(filename, 'w') as final:
            final.write(output)
            print(f'Backup of {hostname} completed successfully')
            print('#' * 30)

        print('Closing connection')
        net_con.disconnect()


send_com()
