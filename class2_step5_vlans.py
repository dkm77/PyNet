import yaml
from netmiko import ConnectHandler


with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()
    devices = yaml.safe_load(content)


CONFIG_FILE = "vlans.txt"


for dev in (
        devices["nxos1"],
        devices["nxos2"],
):
    print("\n\nconnecting to")
    print(dev)
    con = ConnectHandler(**dev)

    print("Prompt", con.find_prompt(), "\n")

    print(f"sending config from file \"{CONFIG_FILE}\"")
    output = con.send_config_from_file(config_file=CONFIG_FILE)

    print()
    print(output)
    print()

    output2 = con.save_config()
    print(output2)

    con.disconnect()
