from ciscoconfparse import CiscoConfParse

conf_obj = CiscoConfParse("class3_step7_conf.txt")
peer_lines = conf_obj.find_objects_w_child(parentspec=r"neighbor .+", childspec=r"remote-as")

bgp_peers = []
for line in peer_lines:
    peer_ip = line.text.replace("neighbor", "").strip()
    peer_remote_as = line.re_search_children("remote-as")[0].text.replace("remote-as", "").strip()
    bgp_peers.append((peer_ip, peer_remote_as))

print(bgp_peers)
