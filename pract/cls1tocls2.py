'''
class A:
    def fn1(self,a,b):
	print a+b

class b:
    def fn2(self):
	A.fn1(self,3,4)
	
b1=b()
b1.fn2()
'''
class A:
    def m(self, x, y):
        print(x+y)

class B:
    def call_a(self):
        A.m(self, 1, 2)

b = B()
b.call_a()
