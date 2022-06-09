import json
from pprint import pprint


with open("class3_step4_data.json", "r") as f:
    content = f.read()

data_dict = json.loads(content)

out_dict = {}
for nei in data_dict["ipV4Neighbors"]:
    out_dict[nei["address"]] = nei["hwAddress"]

pprint(out_dict)
