from getpass import getpass

from netmiko import ConnectHandler

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


net_connect = ConnectHandler(device_type='cisco_ios', ip='192.168.122.11', username='puma', password=password_1)
output = net_connect.send_command("show ip int brief")
if "FastEthernet1/10" and 'down' in output:
    print(output)
    net_connect.enable()
    net_connect.send_config_set(["int fa1/10", "no shutdown"])

else:
    print("Int_Fa1/10 is still down")

print('*' * 100)
print(output)
net_connect.disconnect()
