# Python3 program to check if given
# number is power of 4 or not 
 
# Function to check if x is power of 4
def isPowerOfFour(n):
    if (n == 0):
        return False
    while (n != 1):
            if (n % 2 != 0):
                return False
            n = n // 2
             
    return True
 
# Driver code
test_no = 8
if(isPowerOfFour(8)):
    print(test_no, 'is a power of 4')
else:
    print(test_no, 'is not a power of 4')
 
# This code is contributed by Danish Raza
