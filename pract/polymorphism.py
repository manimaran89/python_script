class addition():
    def __init__(self,a,b):
	self.a = a
	self.b = b

    def add(self):
	print self.a+self.b

class subtract():
    def __init__(self,a,b):
        self.a = a
        self.b = b
	
    def add(self):
        print self.a + self.b 	

def total(calc):
    calc.add()

add1=addition(20,3)
add2=subtract(20,5)

total(add1)
total(add2)
