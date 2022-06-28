def wordSleuth(dict_file,grid):
    # เก็บตัวอักษรจากไฟล์ dictionary มาใส่ใน list
    word_in_dict_file = open(dict_file, "r")
    list_of_dictionary = []
    for x in word_in_dict_file:
        x = x.replace("\n","")
        # ทำให้เป็นตัวเล็กให้หมด
        x = x.lower()
        list_of_dictionary.append(x)

    # เก็บตัวอักษรจากไฟลื grid มาใส่ใน list
    word_grid = open(grid, "r")
    list_of_grid = []
    for x in word_grid:
        x = x.replace("\n","")
        # ทำให้เป็นตัวเล็กให้หมด
        x = x.lower()
        x = x.split(" ")
        list_of_grid.append(x)

    ans_list = []

    # ทำ list ของ grid แยกเป็นแถวนอน แถวตั้ง แถวทแยงมุม
    horizon_list = []
    vertical_list = []
    diagonal_list = []

    # ทำแถวนอน
    for i in list_of_grid:
        horizon_list.append("".join(i))

    # ทำแถวตั้ง
    temp2=[]
    for i in range(len(list_of_grid)):
        temp1 = []
        for j in range(len(list_of_grid)):
            temp1.append(list_of_grid[j][i])
        temp2.append(temp1)
    
    for i in temp2:
        vertical_list.append("".join(i))

    # ทำแแถวทแยงมุม i*i
    temp4 = []
    for i in range(len(list_of_grid)):
        temp4.append(list_of_grid[i][i])
    diagonal_list.append("".join(temp4))

    # ทำแถวทแยงมุมส่วนที่เหลือ (ครึ่งบน)
    max_right = len(list_of_grid)-1
    g = 1
    for i in range(max_right):
        temp3 = []
        for k in range(max_right):
            j = k+g
            temp3.append(list_of_grid[k][j])
        diagonal_list.append("".join(temp3))
        max_right = max_right-1
        g = g+1

    # ทำแถวทแยงมุมส่วนที่เหลือ (ครึ่งล่าง)
    max_right = len(list_of_grid)-1
    g = 1
    for i in range(max_right):
        temp3 = []
        for k in range(max_right):
            j = k+g
            temp3.append(temp2[k][j])
        diagonal_list.append("".join(temp3))
        max_right = max_right-1
        g = g+1

        for i in list_of_dictionary:
            for j in horizon_list:
                if i in j:
                    ans_list.append(i)
            for k in vertical_list:
                if i in k:
                    ans_list.append(i)
            for p in diagonal_list:
                if i in p:
                    ans_list.append(i)
    
    return sorted(list(set(ans_list)))


# เปลี่ยน directory ให้เป็น path ที่เก็บไฟล์ dictionary กับ puzzle
print(wordSleuth(r"C:\Users\chano\Desktop\python project\sheet\final\dictionary.txt",r"C:\Users\chano\Desktop\python project\sheet\final\puzzle.txt"))