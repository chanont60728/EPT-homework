class Matrix2():
    def __init__(self):
        self.E11=0
        self.E12=0
        self.E21=0
        self.E22=0
    def add(self,v):
        total_sum = Matrix2()
        total_sum.E11 = self.E11+v.E11
        total_sum.E12 = self.E12+v.E12
        total_sum.E21 = self.E21+v.E21
        total_sum.E22 = self.E22+v.E22
        return total_sum
    def minus(self,v):
        total_minus = Matrix2()
        total_minus.E11 = self.E11-v.E11
        total_minus.E12 = self.E12-v.E12
        total_minus.E21 = self.E21-v.E21
        total_minus.E22 = self.E22-v.E22
        return total_minus
    def mul(self,v):
        total_mul = Matrix2()
        total_mul.E11 = (self.E11*v.E11) + (self.E12*v.E21)
        total_mul.E12 = (self.E11*v.E12) + (self.E12*v.E22)
        total_mul.E21 = (self.E21*v.E11) + (self.E22*v.E21)
        total_mul.E22 = (self.E21*v.E12) + (self.E22*v.E22)
        return total_mul
    def det(self):
        determinant = (self.E11*self.E22) - (self.E12*self.E21)
        return determinant
    def minor(self,i,j):
        if i==1 and j==1:
            mi = self.E22
        elif i==1 and j==2:
            mi = self.E21
        elif i==2 and j==1:
            mi = self.E12
        else:
            mi = self.E11
        return mi
    def cof(self,i,j):
        cofactor = ((-1)**(i+j))*self.minor(i,j)
        return cofactor
    def adj(self):
        adj_matrix = Matrix2()
        adj_matrix.E11 = self.cof(1,1)
        adj_matrix.E12 = self.cof(2,1)
        adj_matrix.E21 = self.cof(1,2)
        adj_matrix.E22 = self.cof(2,2)
        return adj_matrix
    def inverse(self):
        result = Matrix2()
        result.E11 = (1/self.det())*self.E22
        result.E12 = (1/self.det())*self.E12*(-1)
        result.E21 = (1/self.det())*self.E21*(-1)
        result.E22 = (1/self.det())*self.E11
        return result