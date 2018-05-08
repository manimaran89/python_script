word="Maani"
count=1
length=""
for i in range(1,len(word)):
    if word[i-1]==word[i]:
       count+=1
    else :
        length += word[i-1]+str(count)+""
        count=1
# length += ("and "+word[i]+" repeats "+str(count))
length += (word[i]+""+str(count))
print (length)
