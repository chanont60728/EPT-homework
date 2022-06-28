# การใช้โปรแกรมนี้ (สำหรับผู้ตรวจ)
# เนื่องจากใน test case จะมี list ที่ยืดหยุ่นได้ ผู้เรียนจึงได้เขียน
# 1. ให้รับค่าจำนวนข้อมูลใน list ก่อนแล้วเก็บไว้ในตัวแปร z 
# ดังนั้นในการตรวจจึงขอให้ใส่จำนวนข้อมูลใน list ก่อนเช่น [1,2,1,3] ก็ใส่เลข 4 หรือ [1,2,1,3,4] ก็ใส่เลข 5
# 2. ต่อมาให้ใส่ข้อมูลใน list เช่นใส่ 1 2 1 3 หรือ 1 2 1 3 4 (ซึ่งจะถูกไว้ในตัวแปร num_to_every)
# 3. ต่อมาให้ใส่ตัวเลขที่จะนำมาเทียบว่าอยู่ใน list (ที่จะถูกแบ่งออกมาเป็นคู่) หรือไม่ เช่นให้ใส่ 1 หรือ 2 หรือ 1 (ซึ่งจะถูกไว้ในตัวแปร x)

def isEverywhere(a,b):
    sublist_summary = []
    for i in range(0,len(a)):
        sublist = a[i:i+2]
        sublist_summary.append(sublist)
    sublist_summary.pop(len(sublist_summary)-1)
    
    for j in range(len(sublist_summary)):
        if b in sublist_summary[j]:
            continue
        else:
            return "false"
            break
    return "true"

every = []

z = int(input("ใส่จำนวนข้อมูลใน list: "))
for i in range(z):
    num_to_every= int(input("ใส่ตัวเลขเพื่อเข้าเป็นข้อมูลใน list: "))
    every.append(num_to_every)
    filled_every = every[:]


x = int(input("ใส่ยอดที่จะเป็นเลขเทียบกับ list : "))

print(isEverywhere(filled_every,x))