from netmiko import ConnectHandler

router = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',
    'username': 'cisco',
    'password': 'cisco',
}

sshCli = ConnectHandler(**router)

# Ejecutar el comando 'show ip interface brief' en el dispositivo remoto
output = sshCli.send_command("show ip interface brief")

# Imprimir la salida
print("show ip interface brief:\n{}".format(output))
