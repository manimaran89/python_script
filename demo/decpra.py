def deco(func):
    def inner():
	print "Inside Decorator"
	func()
    return inner

@deco
def fun1():
    print "Inside function"

fun1()
