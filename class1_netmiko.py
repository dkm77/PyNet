import json
import yaml
from netmiko import ConnectHandler


f = open("/home/kuhlmann/.netmiko.yml")
content = f.read()
devices = yaml.safe_load(content)
f.close()

# print(json.dumps(devices, indent=4))
# dev = devices["nxos1"]

output_file = open("output", "w")

for dev in (devices["nxos1"], devices["nxos2"]):
    print("\n\nconnecting to", dev)
    con = ConnectHandler(**dev)

    print("Prompt", con.find_prompt(), "\n")


    command = "show version"
    print(f"sending {command}")
    output = con.send_command(command)

    print("writing output to file")
    output_file.write(f"***** {dev['host']} *****\n\n{output}\n\n\n")

output_file.close()
