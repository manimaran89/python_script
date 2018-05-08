'''
def missing_number(num_list):
    c = range(num_list[0],num_list[-1]+1)
    print c
    return sum(range(num_list[0],num_list[-1]+1)) - sum(num_list)

print(missing_number([1,2,3,4,6,7,8]))
'''
def missing_no_from_list(nos):
    maximum = max(nos) # or last element (nos[-1] + 1)
    l = set(range(1, maximum+1))
    print l
    return list((l ^ set(nos)))

print missing_no_from_list([1, 3, 5, 9, 15])
