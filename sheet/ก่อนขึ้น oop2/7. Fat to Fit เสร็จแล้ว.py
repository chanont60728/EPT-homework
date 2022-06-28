def new_avg(a,b):
    x = (b*(len(a)+1)) - sum(a)
    if x>0:
        return int(x)
    else:
        return "ERROR !!! ค่า average ที่มีมากกว่าค่า average ที่ต้องการไปแล้ว"

donation_list = []
while True:
    n = int(input("ใส่ตัวเลขเข้า donation list เป็นจำนวนเต็มบวกที่มากกว่า 0 (และกด 9999 เพื่อหยุดใส่): "))
    if n == 9999:
        break
    elif n<=0:
        print("การบริจาคไม่ควรเกิดยอด 0 หรือติดลบ ให้ใส่จำนวนเต็มบวกเท่านั้น")
    else:
        donation_list.append(n)
target = int(input("ใส่ค่า average ที่ต้องการ: "))

print(new_avg(donation_list,target))


