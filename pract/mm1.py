class mango:
    def func(self):
        a, b = 8, 9
        return a+b
 
    def func2(self, x,y):
        c = self.func()
        z = x + y + c
        return z
 
a = mango().func2(1,1)
print(a)
