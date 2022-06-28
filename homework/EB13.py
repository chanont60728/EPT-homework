# สมชายดูมายากล
list_of_ABC = []
n=input("ให้รับค่าเป็น A หรือ B หรือ C ไม่เกิน 50 ตัวเท่านั้น : ")
list_of_ABC.extend(list(n))

position = "left"

for i in list_of_ABC:
    if position == "left":
        if i=="A":
            position = "mid"
        elif i=="C":
            position = "right"
        continue
    
    if position == "mid":
        if i=="A":
            position = "left"
        elif i=="B":
            position = "right"
        continue

    if position == "right":
        if i=="B":
            position = "mid"
        elif i=="C":
            position = "left"
        continue
    else:
        pass

if position=="left":
    print(1)
elif position=="mid":
    print(2)
elif position=="right":
    print(3)
else:
    pass
