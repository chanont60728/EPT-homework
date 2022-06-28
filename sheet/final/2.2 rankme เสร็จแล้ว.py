list_of_A = []
def rank(A:list,X:int):
    count = 0
    for i in A:
        if i<=X:
            count += 1
    return count

while True:
    to_list_A = int(input("ใส่ตัวเลขเพื่อเก็บเข้าตัวเลขเข้า list A (หรือใส่ -999 เพื่อหยุดใส่ค่าเข้า list A) : "))
    if to_list_A == -999:
        break
    else:
        list_of_A.append(to_list_A)

to_X = int(input("ใส่ตัวเลขเพื่อเก็บเป็นเข้า X: "))

print(rank(list_of_A,to_X))
