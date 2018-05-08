import json
json_obj = json.load(json1)

ips = []
for piece in json_obj['data']:
    this_ip = [piece['custom3'], piece['modemId']]
    ips.append(this_ip)
    print ips
