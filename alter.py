a=range(10)
def fun1(a):
    c=a
    c.reverse()
    for i in c:
        yield i

def fun2(a):
    b=a
    for j in b:
        yield j

m1=[]
s1=fun1(a)
s2=fun2(a)

for i in range(int(len(a)/2)):
	m1.append(s1)
	m1.append(s2)
	

print m1

