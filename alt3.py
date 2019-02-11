asd=[1,2,3,4,5]
out=[]
print asd
while asd:
   out.append(asd.pop(0))
   #print out
   try:
       out.append(asd.pop())
       #print out	
   except Exception:
       pass
print out
