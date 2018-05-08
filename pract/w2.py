with open("content.txt","r") as f:
    for line in f:
	with open("out.txt","w") as f1:
	    f1.writelines(line)
