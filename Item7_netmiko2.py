#item7 interfaces
from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',
    'username': 'cisco',
    'password': 'cisco',
}

sshCli = ConnectHandler(**router)

output = sshCli.send_command("show ip interface brief")

print("show ip interface brief:\n{}".format(output))