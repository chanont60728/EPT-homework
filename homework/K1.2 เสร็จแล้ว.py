A = [[0,0,0],[0,0,0],[0,0,0]]
B = [[0,0,0],[0,0,0],[0,0,0]]
C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = int(input("ใส่ค่าเข้า matrix A: "))

for k in range(len(B)):
    for l in range(len(B[0])):
        B[k][l] = int(input("ใส่ค่าเข้า matrix B: "))

for i in range(len(A)):
    for j in range(len(A[0])):
        s=0
        for k in range(len(A[0])):
            s=s+A[i][k]*B[k][j]
        C[i][j]=s
print(C)