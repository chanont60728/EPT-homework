def fibo(n):
    if n <= 1:
        return n
    else:
        return(fibo(n-1) + fibo(n-2))

def writeAllfiboTo(n):
    global fibo_list
    fibo_list = []
    for i in range(1,n):
        fibo_list.append(fibo(i))
    return fibo_list

def isInFiboSequence(k):
    if k in writeAllfiboTo(k):
        return True
    else:
        return False

n_th_of_fibo = int(input("ใส่จำนวน sequence ให้ fibonacci: "))
writeAllfiboTo(n_th_of_fibo)
print("ลำดับของ fibonacci sequence จำนวนเท่าที่ใส่เลขจำนวนมีดังนี้")
print(fibo_list)

check = int(input("ใส่จำนวนที่จะตรวจสอบ (ลำดับไม่เกิน fibonacci sequence ที่มี): "))
print(isInFiboSequence(check))



