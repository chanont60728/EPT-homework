class Fraction():
    def __init__(self,n,d):
        self.n = n
        self.d = d

    # ปรับให้เป็นเศษส่วนอย่างต่ำ
    def reduce(self):
        f = Fraction(self.n,self.d)
        f.n = self.n
        f.d = self.d
        for i in range(self.d,1,-1):
            if self.d%i==0 and self.n%i==0:
                f.n = self.n / i
                f.d = self.d / i
                return f
        return f

    def add(self,f):
        total_plus = Fraction(self.n,self.d)
        if f.d == self.d:
            total_plus.n = self.n+f.n
            total_plus.d = self.d
        else:
            total_plus.n = (self.n*f.d)+(self.d*f.n)
            total_plus.d = self.d*f.d
        return total_plus.reduce()

    def multiply(self,f):
        total_mul = Fraction(self.n,self.d)
        if (self.n*f.n < 0 and self.d*f.d>0) or (self.n*f.n > 0 and self.d*f.d<0):
            total_mul.n = abs(self.n*f.n)*(-1)
            total_mul.d = abs(self.d*f.d)            
        else:
            total_mul.n = abs(self.n*f.n)
            total_mul.d = abs(self.d*f.d)
        return total_mul.reduce()
    
    def subtract(self,f):
        total_minus = Fraction(self.n,self.d)
        if f.d == self.d:
            total_minus.n = self.n-f.n
            total_minus.d = self.d
        else:
            total_minus.n = (self.n*f.d)-(self.d*f.n)
            total_minus.d = self.d*f.d        
        return total_minus.reduce()

    def divide(self,f):
        total_div = Fraction(self.n,self.d)
        if (self.n*f.d < 0 and self.d*f.n>0) or (self.n*f.d > 0 and self.d*f.n<0): 
            total_div.n = abs(self.n*f.d)*(-1)
            total_div.d = abs(self.d*f.n)
        else:
            total_div.n = abs(self.n*f.d)
            total_div.d = abs(self.d*f.n)
        return total_div.reduce()        


a = int(input("ใส่ค่าตัวเลข a เป็นค่าเริ่มต้น (เศษ): "))
b = int(input("ใส่ค่าตัวเลข b เป็นค่าเริ่มต้น (ส่วน): "))

default_Fraction = Fraction(n=a,d=b)

c = int(input("ใส่ค่าตัวเลข c เป็นค่าเปรียบเทียบ (เศษ): "))
d = int(input("ใส่ค่าตัวเลข d เป็นค่าเปรียบเทียบ (ส่วน): "))

f = Fraction(n=c,d=d)

print("ผลบวกของ a กับ b คือ",default_Fraction.add(f).n,"/",default_Fraction.add(f).d)
print("ผลลบของ a กับ b คือ",default_Fraction.subtract(f).n,"/",default_Fraction.subtract(f).d)
print("ผลคูณของ a กับ b คือ",default_Fraction.multiply(f).n,"/",default_Fraction.multiply(f).d)
print("ผลหารของ a กับ b คือ",default_Fraction.divide(f).n,"/",default_Fraction.divide(f).d)
