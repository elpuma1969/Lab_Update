from netmiko import BaseConnection

from Netmiko.base_1 import CiscoIOSConnection


# Create a subclass of BaseConnection for Cisco IOS devices
class CiscoIOSConnection(BaseConnection):
    def __init__(self, *args, **kwargs):
        # Call the parent __init__ method to set up the connection
        super().__init__(*args, **kwargs)

    def connect(self):
        pass

        # Send multiple commands to configure the device
        self.send_command("terminal length 0")
        self.send_command("no logging console")
        self.send_command("logging buffered 1000000")


# Create an instance of the CiscoIOSConnection class
ios_device = {
    "device_type": "cisco_ios",
    "ip": "192.168.122.11",
    "username": "puma",
    "password": "cisco",
    "port": 22,
}
conn = CiscoIOSConnection(**ios_device)

# Connect to the device
conn.connect()

# Send a command to the device and print the output
output = conn.send_command("show version")
print(output)

# Close the connection
conn.disconnect()
