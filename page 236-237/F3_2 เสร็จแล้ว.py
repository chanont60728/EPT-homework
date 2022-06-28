import os

#แก้ path file ให้ตรงกับ path ที่เก็บรูปภาพไว้โดยใส่ r ไว้ข้างหน้า และเปลี่ยนจาก secret_python เป็น secret_python2
path = r"C:\Users\chano\Desktop\python project\page 236-237\python_sectet\secret_python2"

old_name_list = []
new_name_list = []

for file in os.listdir(path):
    old_name_list.append(file) #เก็บชื่อตั้งต้นไว้ใน old_list เพื่อรอเปลี่ยน
    file = file.split("_") # แยกเลขตัวหน้ากับตัวหลังออกจากกัน
    new_name_list.append(file[1]) # เอาเลขตัวหลังมาใส่ list ใหม่

os.chdir(path) #เข้าไปใน folder ที่ไฟล์เก็บรูปภาพโจทย์

for i in range(len(new_name_list)):
    os.rename(old_name_list[i],new_name_list[i])
    
# คำตอบจาก secret_python คือ your mother is coming!
# คำตอบจาก secret_python2 คือ Hello, My name is James. I come from Pluto!

