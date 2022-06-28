# วิธีที่ทำให้ code รันได้
# จะต้อง install module Pillow ก่อนโดยพิมพ์ pip install Pillow ใน terminal

from PIL import Image

img = Image.open(r'C:\Users\chano\Desktop\python project\page 236-237\F3_4 original.jpg') #แก้ส่วนนี้ให้เป็น directory ของรูปภาพต้นแบบ
img = img.convert('RGB')
pixels = img.load()

for i in range(img.size[0]):
    for j in range(img.size[1]):
        r,g,b = pixels[i,j]

        r=i+r
        if r>255:
            r=255
        g=j+g
        if g>255:
            g=255
        b=100+b
        if b>255:
            b=255
        
        color = (r,g,b)
        pixels[i,j] = color
img.show()
#img.save(r'C:\Users\chano\Desktop\python project\page 236-237\F3_4 after run.jpg') #แก้ส่วนนี้ให้เป็น directory ที่จะแสดงรูปภาพผลลัพธ์

# ผลลัพธ์ที่ได้จากการรัน code นี้คือจะได้ไฟล์รูปภาพปรากฎขึ้นใน directory ของบรรทัดสุดท้าย img.save(directory)
# รูปภาพที่ปรากฏขึ้นจะเป็นรูปที่แบ่งสีเหลือง แดง เขียว ขาว อย่างชัดเจน โทนสีจะสว่างมาก ตามรูปภาพผลลัพธ์ที่ส่งมาด้วย