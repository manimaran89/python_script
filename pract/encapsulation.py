class encap():
    def __init__(self):
        self.__version =21

    def getVersion(self):
	print self.__version

    def setVersion(self,version):
	self.__version = version
   	print self.__version
obj1 = encap()
obj1.getVersion()
obj1.setVersion(23)
obj1.getVersion()
print obj1.__version

   
