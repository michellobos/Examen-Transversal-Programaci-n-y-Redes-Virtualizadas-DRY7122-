#item7 show run
from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',
    'username': 'cisco',
    'password': 'cisco',
}

sshCli = ConnectHandler(**router)

output = sshCli.send_command("show running-config")

print("show running-config:\n{}".format(output))