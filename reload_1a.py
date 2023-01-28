import time
from netmiko import ConnectHandler


class MyNetmiko:
    def __init__(self, device_type, host, username, password):
        self.device_type = device_type
        self.host = host
        self.username = username
        self.password = password

    def connect(self):
        net_con = ConnectHandler(device_type=self.device_type, host=self.host, username=self.username,
                                 password=self.password)
        return net_con


if __name__ == '__main__':
    with open('avi_device.txt') as f:
        devices_list = f.read().splitlines()

    for devices in devices_list:
        print('Connecting to device" ' + devices)
        ip_address_of_device = devices
        ios_device = {
            'device_type': 'cisco_ios',
            'ip': ip_address_of_device,
            'username': 'puma',
            'password': 'cisco',
            'port': 22
        }

        connection = ConnectHandler(**ios_device)

        command_1 = 'reload'
        output = connection.send_command_timing(command_1, strip_prompt=False, strip_command=False, delay_factor=4,
                                                read_timeout=1000)

        if "Proceed with reload" in output:
            output += connection.send_command_timing("y", strip_prompt=False, strip_command=False, delay_factor=4,
                                                     read_timeout=1000)
            time.sleep(25)
        connection.disconnect()
        print(output)




