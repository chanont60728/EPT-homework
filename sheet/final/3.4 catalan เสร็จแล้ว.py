def Catalan(n):
    if n <= 1:
        return 1
 
    res = 0
    for i in range(n):
        res += Catalan(i) * Catalan(n-i-1)
 
    return res

ans_list = []
n = int(input("ใส่ค่า n: "))

for i in range(n+1):
    ans_list.append(Catalan(i))

print(ans_list)