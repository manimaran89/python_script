def fibo(num_range):
    a,b = 0,1
    for i in range(0,num_range):
	yield a
	a,b = b,a+b

for item in fibo(10):
    print item
