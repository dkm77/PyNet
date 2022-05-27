import time
import yaml
from netmiko import ConnectHandler


with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()
    devices = yaml.safe_load(content)


CONFIG_FILE = "vlans.txt"


dev = devices["cisco4"]

dev["secret"] = dev["password"]
dev["session_log"] = "my_output.txt"


print("\n\nconnecting to")
print(dev)
con = ConnectHandler(**dev)

print("a) Prompt", con.find_prompt(), "\n")

output = con.config_mode()
print(f"b) {output}")
print("Prompt", con.find_prompt(), "\n")

output = con.exit_config_mode()
print(f"c) {output}")
print("Prompt", con.find_prompt(), "\n")

output = con.write_channel("disable\n")
print(f"d) {output}")

time.sleep(2)
output = con.read_channel()
print(f"e) {output}")

output = con.enable()
print(f"f) {output}")
print("Prompt", con.find_prompt(), "\n")

con.disconnect()

print("\n\nSession Log:\n")
with open(dev["session_log"]) as f:
    print(f.read())
