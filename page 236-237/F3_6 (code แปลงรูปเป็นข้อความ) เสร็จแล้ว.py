# จะต้องมีรูปภาพที่ถูกเปิดขึ้นจากการรันไฟล์ "F3_6 สร้างรูปภาพ" ก่อน แล้วรูปภาพนั้นจะต้องอยู่ใน directory เดียวกันกับ img = Image.open() ในไฟล์นี้

from PIL import Image
import sys

img = Image.open(r'C:\Users\chano\Desktop\F3_6 after run.png')
# ให้เปลี่ยน directory เป็น directory ที่เดียวกันกับในไฟล์ (F3_6 code สร้างรูปภาพ)
pixels = img.load()

width , height = img.size
for i in range(height):
    r, g, b = pixels[0,i]
    sys.stdout.write(chr(r))


