a=[1,2,4,5]

b=[a[i] for i in range(1,len(a))]
print b

c=[a[0]]
print c
b.extend(c)
print b
