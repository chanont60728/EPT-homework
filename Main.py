from MatrixN import MatrixN

N = int(input())
E = []
for i in range(N):
    col = []
    for j in range(N):
        col.append(float(input()))
    E.append(col)
    
v1 = MatrixN(N,E)

E = []
for i in range(N):
    col = []
    for j in range(N):
        col.append(float(input()))
    E.append(col)
    
v2 = MatrixN(N,E)

result = v1.mul(v2)
result.printMyMatrix()



