num = 0
with open("content.txt","r") as f:
    for line in f:
	words=line.split()
	num += len(words)
print "Number of words:",num
