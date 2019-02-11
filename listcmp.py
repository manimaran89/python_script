tinylist =[123,'john',2.23]
list1 =[123,'xyz',2.23]
print "******************\n"
for item in list1:
	for item1 in tinylist:
		if item == item1:
			print item
		else:
			print "No match"
