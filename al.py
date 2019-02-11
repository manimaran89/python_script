a=[0,1,2,3,4,5,8,9]
l = []
print a
if(int(len(a)) % 2 == 0):
    for i in range(int((len(a))/2)):
	l.append(a[i])
	l.append(a[(len(a) - 1) - i])
    else:
        #print("List length is not even")
        print(l)
