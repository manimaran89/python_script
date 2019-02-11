import re
N = int(raw_input())
number = [raw_input() for i in range(N)]
check = lambda no:len(re.findall("^[7-9]\d{9}$",no))
print "--check--"
print check
print "--check--"
match = map(check, number)

print "---number---"
print number
print "---number---"
print "---match---"
print match
print "---match--"
for i in match:
    if i == 1:
        print "YES"
    else:
        print "NO"
