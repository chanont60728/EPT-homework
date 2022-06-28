n = [-2,11,-4,-2,-3,10,100,-200]
total = 0

#เช็คว่าค่าที่มากที่สุดใน list มากกว่า 0 หรือไม่ 
#ถ้าใช่ให้ loop แล้วเอาค่าบวก
if max(n)>0:
    for i in n:
        if i>0:
            total = total+i
    print(total)

#ถ้าไม่ใช่ ให้ print ค่าที่มากที่สุดออกมา
else:
    print(max(n))
