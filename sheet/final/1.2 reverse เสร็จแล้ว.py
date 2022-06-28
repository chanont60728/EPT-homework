def rev(n:str):
    n = n[::-1]
    return int(n)

get_num = int(input("ใส่ตัวเลข: "))
get_num = str(get_num)
print(rev(get_num))