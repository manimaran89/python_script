import re
b="abcdefghijklmnopqrstuvwxyz"
d=re.match('^/^[A-z]+$/',b)
print d
if d == None:
    print "Mismatch"
else:
    print "Matched with all alphabets"
