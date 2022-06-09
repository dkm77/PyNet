import yaml
from pprint import pprint

with open("/home/kuhlmann/.netmiko.yml") as f:
    content = f.read()

devices = yaml.safe_load(content)
pprint(devices)

with open("out.yaml", "w") as f:
    yaml.dump(devices, f, default_flow_style=True)

with open("out_verbose.yaml", "w") as f:
    yaml.dump(devices, f, default_flow_style=False)
