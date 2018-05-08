import json

param1 = "xxxxxx"
param2 = "bbb"
param3 = "333333333"

with open('data/'+param1+'.json','a') as f:
    test1=[]
    data = param2,
    json.dump(data, f, sort_keys=True, indent=1,ensure_ascii=False)
    test1.append(data)
'''
json_obj = json.load(f)

ips = []
for piece in json_obj['data']:
    this_ip = [piece['custom3'], piece['modemId']]
    ips.append(this_ip)
    print ips
'''
