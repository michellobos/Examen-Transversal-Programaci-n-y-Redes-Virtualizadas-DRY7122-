#item7 EIGRP
from netmiko import ConnectHandler

ios_xe = {
    'device_type': 'cisco_ios',
    'host': '192.168.56.102',
    'username': 'cisco',
    'password': 'cisco',
}

sshCli = ConnectHandler(**ios_xe)
print(sshCli)

config = [
    'router eigrp EXAMEN',
    'address-family ipv4 unicast autonomous-system 7',
    'network 192.168.56.0 0.0.0.255',
    'af-interface default passive-interface',
    'af-interface GigabitEthernet0/1 no passive-interface',
    'exit-address-family',
    'address-family ipv6 unicast autonomous-system 7',
    'af-interface default passive-interface',
    'af-interface GigabitEthernet0/1 no passive-interface',
    'exit-address-family'
]

sshCli.send_config_set(config)
print(sshCli.send_command('show running-config | section eigrp'))
