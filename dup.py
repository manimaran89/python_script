a=[1,2,2,3,3,4,4,4,5]
c=list(set(a))
b=[]
'''
for i in a:
    if i not in b:
	b.append(i)
    elif i in b:
	b.remove(i)
print b
'''

for i in c:
    d=a.count(i)
    b.append(i)
    if i in b and d >= 2:
	b.remove(i)
print b
