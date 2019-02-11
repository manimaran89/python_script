a="Mani maran asm tech"
c=a.split(" ")
print " ".join(c[-1::-1])

#for char in range(len(a) - 1, -1, -1):
    #print a[char]
  #print "".join(a[char])

wordList=list(a)

for i in range( len(wordList) - 1, -1, -1) :
    c= list(wordList[i])
    print "".join(c)	


