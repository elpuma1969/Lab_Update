from netmiko import ConnectHandler
import schedule
from datetime import datetime
import time

user_1 = "puma"
password_1 = 'cisco'


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


def job():
    with open('commands_file.txt') as f:
        f.read().splitlines()

    with open("devices_file.txt") as f:
        devices_list = f.read().splitlines()

    for devices in devices_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': "puma",
            'password': "cisco",
            'secret': "cisco",
            'port': 22,

        }
        net_connect = ConnectHandler(**ios_device)
        print('Entering the enable mode...')

        output = net_connect.send_config_from_file('commands_file.txt')
        print(output)

        prompt = net_connect.find_prompt()
        hostname = prompt[0:-1]

        now = datetime.now()
        year = now.year
        month = now.month
        day = now.day

        filename = f'{hostname}_{year}-{month}-{day}_update.txt'

        with open(filename, 'w') as final:
            final.write(output)
            print(f'Backup of {hostname} completed successfully')
            print('#' * 30)

        print('Closing connection')
        net_connect.disconnect()


schedule.every().day.at("11:54").do(job)


while True:
    schedule.run_pending()
    time.sleep(1)
