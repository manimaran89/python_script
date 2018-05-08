def geo_prog(li):
   diff = li[1]/float(li[0])
   for i in range(1,len(li)):
	if li[i]/float(li[i-1]) != diff:
	    return False
   return True

print geo_prog([3,6,12,24])
print geo_prog([2,3,4,7])
   
