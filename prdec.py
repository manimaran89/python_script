def deco(func):
    def inner(a,b):
	print ("I am going to divide",a,"and",b)
	if b == 0:
	    print ("Cannot Divide a and b")
	    return

	return func(a,b)
    return inner

@deco
def dividor(a,b):
    print a/b

dividor(10,5)
