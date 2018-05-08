'''
def dec_divide(func):
    def inner(a,b):
	print "I am going to divide",a,"and",b
	if b == 0:
	    print "Cannot divide",a,"and",b
	    return 
	return func(a,b)
    return inner

@dec_divide
def divide(a,b):
    print a/b
'''
def smart_divide(func):
   def inner(a,b):
      print("I am going to divide",a,"and",b)
      if b == 0:
         print("Whoops! cannot divide")
         return

      return func(a,b)
   return inner

@smart_divide
def divide(a,b):
    print a/b


divide(10,2)
