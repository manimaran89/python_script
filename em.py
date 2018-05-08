import re

addressToVerify ='inf@mailhippo.com'
ss=str(addressToVerify)
match = re.match('^[_a-z0-9-]+(\.[_a-z0-9-]+)*@[a-z0-9-]+(\.[a-z0-9-]+)*(\.[a-z]{2,4})$', ss)
if match == None:
	print('Bad Syntax')
	raise ValueError('Bad Syntax')

else:
	print "Match"
