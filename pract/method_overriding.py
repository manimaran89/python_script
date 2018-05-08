class mark():
    def __init__(self,mark):
	self.mark = mark

    def printmark(self):
	print self.mark

class child(mark):
    def addonemark(self):
	print self.mark+5

c=child(95)
c.addonemark()


