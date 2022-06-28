# Big O ที่ดี่ที่สุดคือการตัดข้อมูลที่ไม่เกี่ยวข้องออกไปจาก loop ให้มากที่สุดเท่าที่ได้เพื่อไม่ให้โปรแกรมทำงานที่ไม่เกี่ยวข้อง (ซึ่งทำให้การประมวลผลช้า)
k = int(input("ใส่จำนวนเข้าตัวเลข k (เป็นตัวเปรียบเทียบ): "))
n = int(input("ใส่ขนาดของข้อมูล: "))
list_of_n = []

for i in range(n):
    number_in = int(input("ใส่ข้อมูลเข้า list: "))
    if number_in<0:
        print("ใส่จำนวนเต็มบวกเท่านั้น")
        break
    else:
        list_of_n.append(number_in)

# จากข้อมูลที่ให้ใส่ค่าเป็นจำนวนเต็มบวกเท่านั้น
# ตัดข้อมูลที่มีค่ามากกว่า k ออกไปเพื่อไม่ให้อยู่ใน loop เพราะค่าที่มากกว่า k ไม่เกี่ยวข้อง
for a in list_of_n:
    if a>k:
        list_of_n.remove(a)

# ใช้ list ที่ถูกตัดยอดที่มากกว่าค่า k ออกไปแล้วมา loop หาค่าที่บวกกันแล้วเท่ากับ k
count = 0
for a in range(len(list_of_n)):
# ให้ loop ตาม a เพื่อให้คู่ที่บวกกันเท่ากับ k แล้ว ไม่ถูกกลับไปวนซ้ำอีก
    for b in range(a):
        if a == b:
            continue
        if list_of_n[b] + list_of_n[a] == k:
            count=count+1
print("ใน list มี",count,"คู่ที่บวกกันแล้วค่าเท่ากับ k")