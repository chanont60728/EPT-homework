def sumofDigitsSquared(n:int):
    n = str(n)
    n = list(n)
    n = [int(x) for x in n]

    sum = 0
    for i in n:
        sum = sum+i**2
    return ishappy(sum)

def ishappy(n:int):
    if n == 1:
        return True
    elif n == 4:
        return False
    else:
        return sumofDigitsSquared(n)

def happyRank(n:int):
    kth_list = []
    
    for i in range(1,10000):
        if ishappy(i):
            kth_list.append(i)
    
    if n in kth_list:
        return kth_list.index(n)+1
    else:
        return "This number not in happy list 1-10000"


get_num = int(input("ใส่ตัวเลข happy เพื่อหาว่าอยู่ลำดับที่เท่าใด: "))
print(happyRank(get_num))