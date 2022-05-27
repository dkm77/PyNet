import yaml
from netmiko import ConnectHandler


with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()
    devices = yaml.safe_load(content)


for dev in (
        devices["cisco4"],
):
    print("\n\nconnecting to", dev)
    con = ConnectHandler(**dev)

    print("Prompt", con.find_prompt(), "\n")

    complete_output = ""
    for cmd in (
            {"command": "ping", "expect_string": ":", "count": 1},
            {"command": "", "expect_string": ":", "count": 1},
            {"command": "8.8.8.8", "expect_string": ":", "count": 1},
            {"command": "", "expect_string": ":", "count": 5},
    ):
        for i in range(cmd["count"]):
            print(f"sending {cmd['command']}")
            # output = con.send_command_timing(cmd["command"])
            output = con.send_command(cmd["command"], expect_string=cmd["expect_string"])
            complete_output = f"{complete_output}{output}\n"

    print("\noutput:")
    print(complete_output)

    con.disconnect()
