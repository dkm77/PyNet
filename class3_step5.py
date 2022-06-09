import yaml
from netmiko import ConnectHandler


with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()

devices = yaml.safe_load(content)

con = ConnectHandler(**devices["cisco3"])
print("Prompt", con.find_prompt(), "\n")
con.disconnect()
