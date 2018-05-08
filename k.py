my_dict = {2:3, 5:3, 8:9}
print my_dict
new_dict = {}
for k, v in my_dict.items():
    new_dict[v] = k
print new_dict
