import yaml
from datetime import datetime
from netmiko import ConnectHandler


with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()
    devices = yaml.safe_load(content)


dev = devices["cisco4"]

print("\n\nconnecting to", dev)
con = ConnectHandler(**dev)

print("Prompt", con.find_prompt(), "\n")

complete_output = ""

for cmd in (
        {"command": "show version"},
        {"command": "show lldp neighbors"},
):
    print(f"sending {cmd['command']}")

    output = con.send_command(cmd["command"], use_textfsm=True)

    print()
    print(output)
    print(type(output))

    for entry in output:
        if "neighbor" in entry:
            print(f"LLDP Neighbor {entry['neighbor']} is connected through remote port {entry['neighbor_interface']}")

    print()

con.disconnect()
