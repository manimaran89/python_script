def reverse_int(no):
    sign = 1
    if no < 0:	
        sign = -1
        no = -1 * no
    r = str(no)
    return int(r[::-1]) * sign

print reverse_int(156)
print reverse_int(-234)
