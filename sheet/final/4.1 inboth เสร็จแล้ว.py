# โจทย์กำหนดว่า list ที่ถูกนำเข้ามาจะเป้น unique item (ไม่มีค่าซ้ำ)
def in_both(x:list,y:list):
    x.sort()
    y.sort()
    dict_of_y = {}
    for i in y:
        dict_of_y[i] = 0

    ans_list = []
    for j in x:
        if j in dict_of_y:
            ans_list.append(j)

    return ans_list

list_of_x = []
while True:
    to_list_x = int(input("ใส่ค่าเก็บเข้า list x หรือใส่ -999 เพื่อหยุดใส่: "))

    if to_list_x == -999:
        break
    else:
        list_of_x.append(to_list_x)

list_of_y = []
while True:
    to_list_y = int(input("ใส่ค่าเก็บเข้า list y หรือใส่ -999 เพื่อหยุดใส่: "))

    if to_list_y == -999:
        break
    else:
        list_of_y.append(to_list_y)

list_of_x = list(set(list_of_x))
list_of_y = list(set(list_of_y))

print(in_both(list_of_x,list_of_y))