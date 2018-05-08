def is_perfect_square(n):
    x = n // 2
    print x
    y = set([x])
    print y
    while x * x != n:
        x = (x + (n // x)) // 2
        if x in y: return False
        y.add(x)
	print y
    print y
    return True

#print(is_perfect_square(8))
print(is_perfect_square(9))
#print(is_perfect_square(100))
