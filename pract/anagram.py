
a="anagram"
b="nagarsm"

w1=list(a)
w2=list(b)
w1.sort()
w2.sort()
if w1 == w2:
    print "string is anagram"
else:
    print "It's not anagram"     

'''
def anagram_word(word1,word2):
    list_w1=list(word1)
    list_w2=list(word2)
    list_w1.sort()
    list_w2.sort()
    return 
'''
