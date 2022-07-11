import mysql.connector
mydb = mysql.connector.connect(
    host = "localhost",
    user = "root",
    password = "",
    database = "HORPAK" ### ถ้าเปลี่ยนชื่อ database ก็ต้องเปลี่ยนตรงนี้ด้วย ###
)

print("เชื่อมต่อ database แล้ว")

# เป็นการเปิดให้ใช้คำสั่ง SQL ผ่าน py ได้ >>>> cursor.execute("ใส่คำสั่ง SQL")
cursor = mydb.cursor()

# สร้าง database (ใช้ครั้งเดียว หลังสร้าง database แล้วให้ comment code ไว้)
#cursor.execute("CREATE DATABASE HORPAK")
#print("สร้าง database แล้ว")

# สร้าง ตาราง (ใช้ครั้งเดียว หลังสร้างตาราง แล้วให้ comment code ไว้)
### ตารางลูกค้า
cursor.execute("CREATE TABLE CLIENT_DETAIL(\
    ClientID int PRIMARY KEY not null,\
    Firstname varchar(40) not null,\
    Lastname varchar(40))")
print("สร้างตารางลูกค้าแล้ว")

### ตารางหอพัก
cursor.execute("CREATE TABLE HORPAK(\
    horpak_and_room_id varchar(40) PRIMARY KEY not null,\
    horpak_name varchar(10) not null,\
    room_number int not null,\
    ClientID int not null)")
print("สร้างตารางหอพักแล้ว")