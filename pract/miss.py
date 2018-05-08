def miss(num):
    maxi = max(num)
    x=set(range(1,maxi+1))
    print x
    x1=list(x)
    print x1
    print num
    a=[]
    for i in x1:
        if i not in num:
	    a.append(i)
    print a
 

miss([1,2,3,9,14])
