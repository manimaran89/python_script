
def star(func):
    def inner(*args,**kwargs):
	print "*************************"
	func(*args,**kwargs)
	print "*************************"
    return inner

def percentage(func):
    def inner(*args,**kwargs):
	print "%%%%%%%%%%%%%%%%%%%%%%%%%"
	func(*args,**kwargs)
	print "%%%%%%%%%%%%%%%%%%%%%%%%%"
    return inner

@star
@percentage
def number(*args, **kwargs):
    print "Printing the number"
    for arg in args:
	print arg

    for kwarg in kwargs:
	print kwarg
		

number(*[1,32,2],a=1)


	
