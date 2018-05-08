class mani:
    def fn1(self):
	a,b=3,1
	c=a+b
	return c

    def fn2(self):
	d=self.fn1()
	m=1+d
	print m

ss=mani()
ss.fn2()
	
