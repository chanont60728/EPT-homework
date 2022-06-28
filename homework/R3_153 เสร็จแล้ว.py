class Fractal():
    def __init__(self):
        self.N = 1
        self.D = 1
    # method reduce คือการปรับให้เป็นเศษส่วนอย่างต่ำ
    def reduce(self):
        f = Fractal()
        f.N = self.N
        f.D = self.D
        for i in range(self.D,1,-1):
            if self.D%i==0 and self.N%i==0:
                f.N = self.N / i
                f.D = self.D / i
                return f
        return f
    
    def add(self,v):
        total_plus = Fractal()
        if v.D == self.D:
            total_plus.N = self.N+v.N
            total_plus.D = self.D
        else:
            total_plus.N = (self.N*v.D)+(self.D*v.N)
            total_plus.D = self.D*v.D
        return total_plus.reduce()
    
    def minus(self,v):
        total_minus = Fractal()
        if v.D == self.D:
            total_minus.N = self.N-v.N
            total_minus.D = self.D
        else:
            total_minus.N = (self.N*v.D)-(self.D*v.N)
            total_minus.D = self.D*v.D        
        return total_minus.reduce()
    
    def mul(self,v):
        total_mul = Fractal()
        if (self.N*v.N < 0 and self.D*v.D>0) or (self.N*v.N > 0 and self.D*v.D<0):
            total_mul.N = abs(self.N*v.N)*(-1)
            total_mul.D = abs(self.D*v.D)            
        else:
            total_mul.N = abs(self.N*v.N)
            total_mul.D = abs(self.D*v.D)
        return total_mul.reduce()

# เรียกใช้ method บวก
test_of_add1 = Fractal()
test_of_add1.N = 3
test_of_add1.D = 10
test_of_add2 = Fractal()
test_of_add2.N = 6
test_of_add2.D = 10
result_add = test_of_add1.add(test_of_add2)
print("เศษจากการบวกเท่ากับ",result_add.N)
print("ส่วนจากการบวกเท่ากับ",result_add.D)

# เรียกใช้ method ลบ
test_of_minus1 = Fractal()
test_of_minus1.N = 3
test_of_minus1.D = 10
test_of_minus2 = Fractal()
test_of_minus2.N = 6
test_of_minus2.D = 10
result_minus = test_of_minus1.minus(test_of_minus2)
print("เศษจากการลบเท่ากับ",result_minus.N)
print("ส่วนจากการลบเท่ากับ",result_minus.D)

# เรียกใช้ method คูณ
test_of_mul1 = Fractal()
test_of_mul1.N = 3
test_of_mul1.D = 10
test_of_mul2 = Fractal()
test_of_mul2.N = 7
test_of_mul2.D = 10
result_mul = test_of_mul1.mul(test_of_mul2)
print("เศษจากการคูณเท่ากับ",result_mul.N)
print("ส่วนจากการคูณเท่ากับ",result_mul.D)