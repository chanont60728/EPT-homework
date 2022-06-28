import numpy as np
# หากเกิด numpy.linalg.LinAlgError: Singular matrix แปลว่า ค่า determinant เป็น 0 และค่าที่ใส่เข้าไปนั้น invert ไม่ได้

A = [[0,0,0],[0,0,0],[0,0,0]]
for i in range(len(A)):
    for j in range(len(A[0])):
        A[i][j] = int(input("ใส่ค่าเข้า matrix A: "))
        
A_numpy = np.array(A)
A_inverse = np.linalg.inv(A_numpy)

B = [[0,0,0],[0,0,0],[0,0,0]]
for k in range(len(B)):
    for l in range(len(B[0])):
        B[k][l] = int(input("ใส่ค่าเข้า matrix B: "))
B_numpy = np.array(B)
B_inverse = np.linalg.inv(B_numpy)

print(A_inverse)
print(B_inverse)