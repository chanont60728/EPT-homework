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
    elif n == 4 :
        return False
    else:
        return sumofDigitsSquared(n)


get_num = int(input("ใส่ตัวเลข: "))
print(ishappy(get_num))
