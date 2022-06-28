A = [[0,0,0],[0,0,0],[0,0,0]]
B = [[0,0,0],[0,0,0],[0,0,0]]
C = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = int(input("ใส่ค่าเข้า matrix A: "))

for k in range(len(B)):
    for l in range(len(B[0])):
        B[k][l] = int(input("ใส่ค่าเข้า matrix B: "))

for m in range(len(C)):
    for n in range(len(C[0])):
        C[m][n] = A[m][n] + B[m][n]

print(C)