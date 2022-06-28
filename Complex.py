import math
class Complex():
    def __init__(self):
        self.a = 0
        self.b = 0
    
    def add(self,v):
        total_plus = Complex()
        total_plus.a = self.a+v.a
        total_plus.b = self.b+v.b
        return total_plus

    def minus(self,v):
        total_minus = Complex()
        total_minus.a = self.a-v.a
        total_minus.b = self.b-v.b
        return total_minus
    
    def mul(self,v):
        total_mul = Complex()
        total_mul.a = (self.a*v.a)-(self.b*v.b)
        total_mul.b = (self.a*v.b)+(self.b*v.a)
        return total_mul

    def div(self,v):
        total_div = Complex()
        total_div.a = ((self.a*v.a)+(self.b*v.b))/((v.a**2)+(v.b**2))
        total_div.b = ((self.b*v.a)-(self.a*v.b))/((v.a**2)+(v.b**2))
        return total_div

    def inv(self):
        total_inv = Complex()
        total_inv.a = self.a / (self.a**2+self.b**2)
        total_inv.b = ((-1)*self.b) / (self.a**2+self.b**2)
        return total_inv

    def conj(self):
        total_conj = Complex()
        total_conj.a = self.a
        total_conj.b = (-1)*self.b
        return total_conj
    
    def size(self):
        vector_z = (self.a**2+self.b**2)**(1/2)
        return vector_z

    def angle(self):
        z = (self.a**2+self.b**2)**(1/2)
        if self.a>0:
            ans = math.atan(self.b/self.a)
        elif self.a<0 and self.b<0:
            ans = math.atan(self.b/self.a)-math.pi
        else:
            ans = math.acos(self.a/z)
        return ans
        
