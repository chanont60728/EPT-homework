n = int(input("ใส่ขนาดตาราง: "))
list_of_n = []
for i in range(n):
    list_of_g = []
    for j in range(n):
        g = int(input("ใส่ตัวเลขเข้าตาราง: "))
        list_of_g.append(g)
    list_of_n.append(list_of_g)    

def checking(n,list_of_n):
    magic_square = 0
    for i in range(n):
        magic_square = magic_square+list_of_n[0][i]

    check4 = 0
    for i in range(n):
        check3 = 0        
        for p in range(n):
            check1 = 0
            check2 = 0
            for q in range(n):
                check1 = check1 + list_of_n[p][q]
                check2 = check2 + list_of_n[q][p]
            if check1!=magic_square or check2!=magic_square:
                return "จาก check 1 กับ check 2 ไม่ใช่ magic square"
            
            check3 = check3 + list_of_n[p][p]
        if check3!=magic_square:
            return "จาก check 3 ไม่ใช่ magic square"

        check4 = check4 + list_of_n[i][n-1-i]
    if check4!=magic_square:
        return "จาก check 4 ไม่ใช่ magic square"
    else:
        return "เป็น magic square"

one_dimension_list = [item for sublist in list_of_n for item in sublist]
check_same_value = set(one_dimension_list)
  
if len(check_same_value) != len(one_dimension_list) :
    print("มีเลขซ้ำ ไม่เป็น magic square")       
else:    
    print(checking(n,list_of_n))
