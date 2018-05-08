class fn1:
    def abc(self):
	print "function 1"

class fn2(object,fn1):
    def sdef(self):
	self.abc()
	print "function2"
b=fn2()
b.sdef()
