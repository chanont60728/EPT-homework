# สร้าง list_of_count เพื่อเก็บจำนวนครั้งก่อนที่ 3x+1 จะมีค่าเท่ากับ 1 ในครั้งแรก
list_of_count = []
for k in range(1,101):
    count = 0
    xn_minus_1 = k

    while True:
        if xn_minus_1%2 == 0:
            xn = xn_minus_1/2
            # ให้นับจำนวนไปเรื่อย ๆ จนกว่า 3x+1 จะมีค่าเท่ากับ 1 ในครั้งแรก
            count = count+1
            if xn == 1:
                list_of_count.append(count)
                break
            xn_minus_1 = xn
        else:
            xn = (3*(xn_minus_1)) + 1
            count = count+1
            if xn == 1:
                list_of_count.append(count)
                break
            xn_minus_1 = xn

# หมายเลข 1 ถึง 101 จะกลายเป็น index ของ list แทน
print("จำนวนครั้งของระหว่างเลข 1 ถึง 100 ที่ทำให้ 3x+1 มีค่าเท่ากับ 1 ในครั้งแรก ตาม list ข้างล่างนี้")
print(list_of_count)

# จะเห็นว่าลำดับการผลิตที่ยาวที่สุดคือ 118 ครั้ง มาจากหมายเลข 97
print("ดังนั้นลำดับการผลิตที่ยาวที่สุดก่อนจบลงที่ 1 คือ")
print(list_of_count.index(max(list_of_count))+1)