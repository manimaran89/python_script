import re
N = int(raw_input())
number = [raw_input() for i in range(N)]
check = lambda no:len(re.findall("^[7-9]\d{9}$",no))
match = map(check, number)
print check
print number
print match
for i in match:
    if i == 1:
        print "YES"
    else:
        print "NO"
