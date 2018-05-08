def sum_of_digit(n):
    tot=0
    while(n>0):
        dig=n%10
        tot=tot+dig
        n=n//10
    return tot
n=int(input("Enter a number:"))
val=sum_of_digit(n)
print val
while len(str(val)) != 1:
    val=sum_of_digit(val)
print("The total sum of digits is:",val)

