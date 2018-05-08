def zero_end(num_list):
    a=[0 for i in range(num_list.count(0))]
    b=[i for i in num_list if i!=0]
    b.extend(a)
    return b

print zero_end([1,2,0,3,4,5,0,0])
print zero_end([1,2,3,0,4])

