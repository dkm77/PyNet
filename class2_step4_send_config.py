import yaml
from datetime import datetime
from netmiko import ConnectHandler

start = datetime.now()

with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()
    devices = yaml.safe_load(content)


dev = devices["cisco3"]

print("\n\nconnecting to", dev)
con = ConnectHandler(**dev)
print(con.fast_cli)
# Cisco-IOS defaults to fast_cli=True and legacy_mode=False
# kwargs.setdefault("fast_cli", True)
# -> Muss also explizit abgeschaltet werden

print("Prompt", con.find_prompt(), "\n")

config_set = [
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
    "ip name-server 1.1.1.1",
    "ip name-server 1.0.0.1",
    "ip domain-lookup",
]

print(f"sending config set:")
for line in config_set:
    print(" "*3, line)

output = con.send_config_set(config_set)

print()
print(output)
print()

# print("*** testing ping ***")
#
# complete_output = ""
# for cmd in (
#         {"command": "ping", "expect_string": ":", "count": 1},
#         {"command": "", "expect_string": ":", "count": 1},
#         {"command": "google.com", "expect_string": ":", "count": 1},
#         {"command": "", "expect_string": ":", "count": 5},
# ):
#     for i in range(cmd["count"]):
#         print(f"sending {cmd['command']}")
#         output = con.send_command(cmd["command"], expect_string=cmd["expect_string"])
#         complete_output = f"{complete_output}{output}\n"
#
# print("\noutput:")
# print(complete_output)

print(f"\n\n----> ran for {datetime.now()-start}")
print(f"\n\n----> disconnecting")
con.disconnect()
