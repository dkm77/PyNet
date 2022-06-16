import json
from pprint import pprint


with open("class3_step3_data.json", "r") as f:
    content = f.read()

data_dict = json.loads(content)

pprint(data_dict)

ipv4_list = []
ipv6_list = []

for if_values in data_dict.values():
    for ipv, prefixes in if_values.items():
        if ipv == "ipv4":
            ipv4_list += prefixes.keys()
        elif ipv == "ipv6":
            ipv6_list += prefixes.keys()

print(ipv4_list)
print(ipv6_list)
