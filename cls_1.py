class A:
    a=5
    b=10
    
    def __init__(self):
	self.a = 70
	self.b = 80

a=A()
print a.a
print a.b
A.a=40
print A.a
print a.a
