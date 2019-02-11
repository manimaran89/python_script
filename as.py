class rec:
   def __init__(self, l,b):
       self.l = l
       self.b = b
   
   def p_l_b(self):
       print self.l
       print self.b

r=rec(12,14)
r.p_l_b()
