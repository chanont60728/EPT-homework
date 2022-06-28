from PIL import Image
import sys

img = Image.open(r"C:\Users\chano\Desktop\python project\page 236-237\hidden_msg_1.bmp")
# ให้เปลี่ยน directory ส่วนนี้ให้เป็นที่เก็บไฟล์รูปภาพ hidden_msg_1.bmp หรือ hidden_msg_2.bmp ไว้เพื่อให้รันได้

rgb_im = img.convert('RGB')

width , height = img.size
for i in range(height):
    r, g, b = rgb_im.getpixel((0, i))
    sys.stdout.write(chr(r))

# คำตอบสำหรับ hidden_msg_1.bmp จะได้ ♫hello hahahah
# คำตอบสำหรับ hidden_msg_2.bmp จะได้ ‼i love you naja!!!
