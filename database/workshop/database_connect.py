import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "horpak" ### ถ้าเปลี่ยนชื่อ database ก็ต้องเปลี่ยนตรงนี้ด้วย ###
)

print("เชื่อมต่อ database แล้ว")

# เป็นการเปิดให้ใช้คำสั่ง SQL ผ่าน py ได้ >>>> cursor.execute("ใส่คำสั่ง SQL")
cursor = mydb.cursor()

# สร้าง database (ใช้ครั้งเดียว หลังสร้าง database แล้วให้ comment code ไว้)
#cursor.execute("CREATE DATABASE HORPAK")
#print("สร้าง database แล้ว")

# สร้าง ตาราง (ใช้ครั้งเดียว หลังสร้างตาราง แล้วให้ comment code ไว้)
cursor.execute("CREATE TABLE CLIENT_DETAIL(\
    ClientID int PRIMARY KEY not null,\
    Date_enter DATE,\
    Firstname varchar(40) not null,\
    Lastname varchar(40))")
print("สร้างตารางแล้ว")
