class Fraction():
    def __init__(self):
        self.N = 1
        self.D = 1
    def reduce(self):
        f = Fraction()
        f.N = self.N
        f.D = self.D
        for i in range(self.D,1,-1):
            if self.D%i==0 and self.N%i==0:
                f.N = self.N / i
                f.D = self.D / i
                return f
        return f
    
    def add(self,v):
        total_plus = Fraction()
        if v.D == self.D:
            total_plus.N = self.N+v.N
            total_plus.D = self.D
        else:
            total_plus.N = (self.N*v.D)+(self.D*v.N)
            total_plus.D = self.D*v.D
        return total_plus.reduce()
    
    def minus(self,v):
        total_minus = Fraction()
        if v.D == self.D:
            total_minus.N = self.N-v.N
            total_minus.D = self.D
        else:
            total_minus.N = (self.N*v.D)-(self.D*v.N)
            total_minus.D = self.D*v.D        
        return total_minus.reduce()
    
    def mul(self,v):
        total_mul = Fraction()
        if (self.N*v.N < 0 and self.D*v.D>0) or (self.N*v.N > 0 and self.D*v.D<0):
            total_mul.N = abs(self.N*v.N)*(-1)
            total_mul.D = abs(self.D*v.D)            
        else:
            total_mul.N = abs(self.N*v.N)
            total_mul.D = abs(self.D*v.D)
        return total_mul.reduce()
    
    def div(self,v):
        total_div = Fraction()
        if (self.N*v.D < 0 and self.D*v.N>0) or (self.N*v.D > 0 and self.D*v.N<0): 
            total_div.N = abs(self.N*v.D)*(-1)
            total_div.D = abs(self.D*v.N)
        else:
            total_div.N = abs(self.N*v.D)
            total_div.D = abs(self.D*v.N)
        return total_div.reduce()

    @staticmethod
    def max(fraction1,fraction2):
        if (fraction1.N/fraction1.D)>(fraction2.N/fraction2.D):
            return Fraction.reduce(fraction1)
        else:
            return Fraction.reduce(fraction2)