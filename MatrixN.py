class MatrixN():
    def __init__(self,n:int=0,e:list=[]):
        self.N = n
        self.E = e
    
    def printMyMatrix(self):
        for i in range(self.N):
            for j in range(len(self.E)):
                print(self.E[i][j])

    def add(self,v):
        result = MatrixN(self.N,self.E)
        for i in range(self.N):
            for j in range(len(self.E)):
                result.E[i][j] = self.E[i][j] + v.E[i][j]
        return result

    def minus(self,v):
        result = MatrixN(self.N,self.E)
        for i in range(self.N):
            for j in range(len(self.E)):
                result.E[i][j] = self.E[i][j] - v.E[i][j]
        return result

    def mul(self,v):
        result = MatrixN(self.N,self.E)
        ans = []
        for i in range(result.N):
            to_list = []
            for j in range(result.N):
                sub_result2 = 0
                sub_list = []
                for k in range(result.N):
                    sub_result2 = sub_result2+(result.E[i][k] * v.E[k][j])
                    sub_list.append(sub_result2)
                to_list.append(sub_list[-1])
            ans.append(to_list)

        real_ans = MatrixN(self.N,ans)
        
        return real_ans      

    def det(self):
        if self.N == 2:
            return (self.E[0][0] * self.E[1][1]) - (self.E[0][1] * self.E[1][0])
        
        else:
            for i in range(len(self.E)):
                self.E[i][i]

