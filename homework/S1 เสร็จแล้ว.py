text1 = input("ใส่ข้อความที่ 1 : ")
text2 = input("ใส่ข้อความที่ 2 : ")

if text2 in text1:
    print("มีข้อความที่ 2 อยู่ในข้อความที่ 1 ตำแหน่งดังนี้")
    print([n for n in range(len(text1)) if text1.find(text2, n) == n])
else:
    print("ไม่มีข้อความที่ 2 อยู่ในข้อความที่ 1")