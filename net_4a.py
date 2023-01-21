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


# Usage
net_connect = MyNetmiko(device_type='cisco_ios', host='192.168.122.11', username=user_1, password=password_1)
conn = net_connect.connect()
print(conn.send_command("show version"))
conn.disconnect()
