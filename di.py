a={'1': 'a', '3': 'a', '2': 'b'}
d=[]

for i,j in a.iteritems():
    #print i
    c=a.get(i)
    #print c	
    d.append(c)
    print d
    for i in d:
        count = d.count(i)
	if count > 1:
	      	
    
