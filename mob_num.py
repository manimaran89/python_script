import re
num="99887766521"
s=len(re.findall("^[7-9]\d{9}$",num))
print s
if s == 1:
    print "Match"
elif s == 0 :
    print "Mismatch"
'''
check=lambda no:len(re.findall("^[7-9]\d{9}$",num))
match =map(check,num)
print match
for i in match:
    if i == 1:
        print "Match"
    else:
        print "Not Match"
'''
