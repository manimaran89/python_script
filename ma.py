'''
def fun1():
    fun1.var = 100
    print(fun1.var)

def fun2():
    print(fun1.var)

fun1()
fun2()

print(fun1.var)

'''

class mani():
    def fun1(self):
        fun1.var = 100
        print(self.fun1.var)

    def fun2(self):
        print(self.fun1.var)
a=mani()
a.fun1()
a.fun2()

