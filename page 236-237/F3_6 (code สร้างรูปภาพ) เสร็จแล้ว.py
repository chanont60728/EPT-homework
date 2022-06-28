from PIL import Image

n = input("ใส่ข้อความที่จะซ่อนไว้ในรูป : ")
hidden_number = []

#ข้อความที่พิมเข้าไปจะถูกซ่อนไว้ในตัว R ของ RGB ของ pixel ลำดับที่ 0 ลงมาเรื่อย ๆ (เป็นลักษณะเดียวกันกับข้อ F3_5)
#ข้อนี้จะ save เป็นไฟล์ png เพื่อไม่ให้ค่า pixel เกิดการเปลี่ยนแปลงตอนที่อ่านค่า pixel จากรูปภาพ (lossless format)
for i in n:
    hidden_number.append(ord(i))

img = Image.new(mode="RGB", size=(400, 400)) #รูปภาพจะสร้างขึ้นจะเป็นรูปสีดำทั้งหมด

pixels = img.load()

for i in range(len(hidden_number)):
    r,g,b = pixels[0,i+1]
    r=hidden_number[i]
    color = r,g,b
    pixels[0,i+1] = color

#img.show()
img.save(r'C:\Users\chano\Desktop\F3_6 after run.png') #สร้างไว้ใน directory ไหนก็ได้แต่ขอให้ตรงกับ directory ที่อยู่ในไฟล์ F3_6 code แปลงรูปเป็นข้อความ

# เมื่อรันไฟล์นี้จะได้รูปภาพสีดำเปล่า ๆ ใน directory ที่อยู่ใน img.save ให้เปิดไฟล์ "F3_6 แปลงรูปเป็นข้อความ" เพื่ออ่านข้อความจากรูป
