class Matrix3():
    def __init__(self):
        self.E=[]
    
    def add(self,v):
        total_add = Matrix3()
        for i in range(3):
            within_total_add =[]
            for j in range(3):
                sum = self.E[i][j]+v.E[i][j]
                within_total_add.append(sum)
            total_add.E.append(within_total_add)
        return total_add

    def minus(self,v):
        total_minus = Matrix3()
        for i in range(3):
            within_total_minus =[]
            for j in range(3):
                sum = self.E[i][j]-v.E[i][j]
                within_total_minus.append(sum)
            total_minus.E.append(within_total_minus)
        return total_minus
    
    def mul(self,v):
        total_mul = Matrix3()
        for i in range(3):
            within_total_mul =[]
            for j in range(1):
                sum_at_left = (self.E[i][j]*v.E[0][j]) + (self.E[i][j+1]*v.E[1][j]) + (self.E[i][j+2]*v.E[2][j])
                sum_at_mid = (self.E[i][j]*v.E[0][j+1]) + (self.E[i][j+1]*v.E[1][j+1]) + (self.E[i][j+2]*v.E[2][j+1])
                sum_at_right = (self.E[i][j]*v.E[0][j+2]) + (self.E[i][j+1]*v.E[1][j+2]) + (self.E[i][j+2]*v.E[2][j+2])
                within_total_mul.append(sum_at_left)
                within_total_mul.append(sum_at_mid)
                within_total_mul.append(sum_at_right)
            total_mul.E.append(within_total_mul)
        return total_mul
    
    def det(self):
        a = self.E[0][0] * ((self.E[1][1]*self.E[2][2]) - (self.E[2][1]*self.E[1][2]))
        b = self.E[0][1] * ((self.E[1][0]*self.E[2][2]) - (self.E[2][0]*self.E[1][2]))
        c = self.E[0][2] * ((self.E[1][0]*self.E[2][1]) - (self.E[2][0]*self.E[1][1]))
        total_det = a-b+c
        return total_det
    
    def minor(self,i,j):
        dict_of_minor ={
            "11" : (self.E[1][1]*self.E[2][2]) - (self.E[1][2]*self.E[2][1]),
            "12" : (self.E[1][0]*self.E[2][2]) - (self.E[2][0]*self.E[1][2]),
            "13" : (self.E[1][0]*self.E[2][1]) - (self.E[2][0]*self.E[1][1]),
            "21" : (self.E[0][1]*self.E[2][2]) - (self.E[2][1]*self.E[0][2]),
            "22" : (self.E[0][0]*self.E[2][2]) - (self.E[2][0]*self.E[0][2]),
            "23" : (self.E[0][0]*self.E[2][1]) - (self.E[2][0]*self.E[0][1]),
            "31" : (self.E[0][1]*self.E[1][2]) - (self.E[1][1]*self.E[0][2]),
            "32" : (self.E[0][0]*self.E[1][2]) - (self.E[1][0]*self.E[0][2]),
            "33" : (self.E[0][0]*self.E[1][1]) - (self.E[1][0]*self.E[0][1])
        }
        result_of_minor = dict_of_minor[str(i)+str(j)]
        return result_of_minor
    
    def cof(self,i,j):
        result_of_cof = ((-1)**(i+j))*self.minor(i,j)
        return result_of_cof

    def adj(self):
        not_tranpose = Matrix3()
        for i in range(1,4):
            within_adj =[]
            for j in range(1,4):
                total = self.cof(i,j)
                within_adj.append(total)
            not_tranpose.E.append(within_adj)

        tranposed = Matrix3()
        for i in range(3):
            within_tranposed =[]
            for j in range(3):
                if i == j :
                    total = not_tranpose.E[i][j]
                    within_tranposed.append(total)
                else:
                    total = not_tranpose.E[j][i]
                    within_tranposed.append(total)
            tranposed.E.append(within_tranposed)       

        return tranposed
        
    def inverse(self):
        inversed_matrix = Matrix3()
        get_det = self.det()
        get_adj = self.adj()

        for i in range(3):
            within_adj =[]
            for j in range(3):
                total = (1/get_det)*get_adj.E[i][j]
                within_adj.append(total)
            inversed_matrix.E.append(within_adj)
        return inversed_matrix    