def eye(n):
    matrix_creation = []

    for i in range(n):
        sub = [0]*n
        sub[i] = 1
        matrix_creation.append(sub)

    return matrix_creation

n = int(input("ใส่ค่า n: "))
print(eye(n))