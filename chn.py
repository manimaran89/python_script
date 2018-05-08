from copy import deepcopy

a=range(6)
b=deepcopy(a)
b.reverse()

def f1(m):
 for i in range(6):
   yield m[i]


def f2(m):
 for i in range(6):
   yield m[i]

f=f1(a)
g=f2(b)

for i in range(3):
 print g.next()
 print f.next()
