import yaml
from datetime import datetime
from netmiko import ConnectHandler


with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()
    devices = yaml.safe_load(content)


dev = devices["nxos2"]

print("\n\nconnecting to", dev)
con = ConnectHandler(**dev, global_delay_factor=2)
con.fast_cli = False

print("Prompt", con.find_prompt(), "\n")

complete_output = ""

for cmd in (
        {"command": "show lldp neighbors detail"},
        {"command": "show lldp neighbors detail", "delay_factor": 8},
):
    start = datetime.now()

    for i in range(5):
        print(f"sending {cmd['command']}")

        if cmd.get("delay_factor") is not None:
            print(f"delay factor {cmd['delay_factor']}")
            output = con.send_command(cmd["command"], delay_factor=cmd["delay_factor"])
        else:
            output = con.send_command(cmd["command"])

    print()
    # print(output)
    print()
    print(f"took {datetime.now()-start}")
    print()

con.disconnect()
