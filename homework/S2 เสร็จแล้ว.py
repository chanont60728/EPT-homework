text1 = input("ใส่ข้อความที่ 1 : ")
text2 = input("ใส่ข้อความที่ 2 : ")
num = int(input("ใส่ตัวเลขตำแหน่งที่จะให้แทรก: "))

text1 = list(text1)

if num > 0:
    text1.insert(num-1,text2)
else:
    text1.insert(num,text2)

for i in text1:
    print(i,end="")