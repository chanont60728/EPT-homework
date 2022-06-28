import re

text = "Chanont Luengprasert"
x = re.findall("t",text)
y = re.findall("ooo",text)

print("พบตัวอักษรที่ค้นหาจำนวนตามใน list =",x)
print("หากไม่พบจะเป็น list เปล่า ๆ =",y)