def putNumbers(n):
    i = 0
    while i<n:
        j=i
        i=i+1
        if j%7==0:
            yield j

#To print the numbers
for i in putNumbers(100):
    print i