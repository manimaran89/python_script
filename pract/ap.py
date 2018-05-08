def ari_pro(li):
    diff=li[1]-li[0]
    for index in range(0,len(li)-1):
	if not(li[index+1] - li[index] == diff):
	   return False
    return True
#	   print "It's Arithmetic Progression"
#	else:
#	   print "Not an Arithmetic Progression"

print ari_pro([1,3,5])
print ari_pro([2,3,7])
