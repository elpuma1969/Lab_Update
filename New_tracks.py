from netmiko import ConnectHandler

def connect_to_switches(device_list):
    for device in device_list:
        connection = ConnectHandler(device_type=device['device_type'], 
                                    ip=device['ip'], 
                                    username=device['username'], 
                                    password=device['password'])
        print(f"Connected to {device['ip']}")
        connection.disconnect()

devices = [
    {'device_type': 'cisco_ios', 'ip': '192.168.1.1', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.2', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.3', 'username': 'admin', 'password': 'secret'}
]

connect_to_switches(devices)



---------------------------------------------------------------------------------------------------------------

def reload_cisco_switches(device_list):
    for device in device_list:
        connection = ConnectHandler(device_type=device['device_type'], 
                                    ip=device['ip'], 
                                    username=device['username'], 
                                    password=device['password'])
        print(f"Connected to {device['ip']}")
        connection.enable()
        output = connection.send_command("reload")
        print(f"Output: {output}")
        connection.disconnect()

devices = [
    {'device_type': 'cisco_ios', 'ip': '192.168.1.1', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.2', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.3', 'username': 'admin', 'password': 'secret'}
]

reload_cisco_switches(devices)

----------------------------------------------------------------------------------------------------------------

def copy_file_to_cisco_switches(device_list, source_file, dest_file):
    for device in device_list:
        connection = ConnectHandler(device_type=device['device_type'], 
                                    ip=device['ip'], 
                                    username=device['username'], 
                                    password=device['password'])
        print(f"Connected to {device['ip']}")
        connection.enable()
        output = connection.send_command(f"copy tftp {source_file} flash:{dest_file}")
        print(f"Output: {output}")
        connection.disconnect()

devices = [
    {'device_type': 'cisco_ios', 'ip': '192.168.1.1', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.2', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.3', 'username': 'admin', 'password': 'secret'}
]

copy_file_to_cisco_switches(devices, 'source_file.bin', 'dest_file.bin')

---------------------------------------------------------------------------------------------------------------

import datetime
from netmiko import ConnectHandler

def backup_cisco_switches(device_list):
    for device in device_list:
        connection = ConnectHandler(device_type=device['device_type'], 
                                    ip=device['ip'], 
                                    username=device['username'], 
                                    password=device['password'])
        print(f"Connected to {device['ip']}")
        running_config = connection.send_command("show run")
        filename = f"{device['ip']}-{datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
        with open(filename, 'w') as f:
            f.write(running_config)
        connection.disconnect()
        print(f"Saved running config to {filename}")

devices = [
    {'device_type': 'cisco_ios', 'ip': '192.168.1.1', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.2', 'username': 'admin', 'password': 'secret'},
    {'device_type': 'cisco_ios', 'ip': '192.168.1.3', 'username': 'admin', 'password': 'secret'}
]

backup_cisco_switches(devices)

---------------------------------------------------------------------------------------------------------------

