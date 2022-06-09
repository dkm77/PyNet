import yaml
from ciscoconfparse import CiscoConfParse
from netmiko import ConnectHandler


with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()

devices = yaml.safe_load(content)

con = ConnectHandler(**devices["cisco4"])
print("Prompt", con.find_prompt(), "\n")

output = con.send_command("show run")
con.disconnect()

conf_obj = CiscoConfParse(output.splitlines())
if_lines = conf_obj.find_objects_w_child(parentspec=r"^interface", childspec=r"ip address .+")

for line in if_lines:
    print(f"Interface Line: {line.text}")
    for ip_line in line.re_search_children("ip address"):
        print(f"IP Address Line: {ip_line.text}")
