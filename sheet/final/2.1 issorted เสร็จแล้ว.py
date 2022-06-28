def issorted(l:list):
    for i in range(len(l)-1):
        if l[i+1] < l[i]:
            return False
    return True

list_of_l = []
while True:
    get_to_list = int(input("ใส่ตัวเลขเข้า list หรือกด -999 เพื่อหยุดการเพิ่มเข้า list: "))
    if get_to_list == -999:
        break
    else:
        list_of_l.append(get_to_list)

print(issorted(list_of_l))
