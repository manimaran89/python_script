a=[1,2,1,1,3,4,4,5]
c=[]
'''
for i in a:
    if i not in c:	
        c.append(i)
print c
'''
for i in a:
    if i in c:
        c.remove(i)
    else:
	c.append(i)
print c    
