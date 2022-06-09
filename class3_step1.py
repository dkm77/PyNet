from pprint import pprint


HEADER_MAPPINGS = {
    "Address": "ip_addr",
    "Hardware Addr": "mac_addr",
    "Interface": "interface",
}


with open("class3_step1_data.txt", "r") as f:
    data = f.read()

arp_list = []
headers = None
for line in data.splitlines():
    if line.startswith("Protocol"):
        # Rename headers
        for k, v in HEADER_MAPPINGS.items():
            line = line.replace(k, v)

        headers = line.split()

    elif headers is not None:
        cols = line.split()

        arp_entry = {}
        for header, col in zip(headers, cols):
            # Skip headers
            if header in HEADER_MAPPINGS.values():
                arp_entry[header] = col
        arp_list.append(arp_entry)

pprint(arp_list)
