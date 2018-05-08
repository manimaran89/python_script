def deco1(func):
    def inner():
	print "Inside Decorator"
        func()
    return inner
@deco1 
def function1():
    print "Inside function"

function1()
