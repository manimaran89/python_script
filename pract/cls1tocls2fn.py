class A:
    def a_function(self):
        print "function from a"

class B(object,A):
    def b_function(self):
	self.a_function()
        print "fuction from b"

ss=B()    
ss.b_function() 

