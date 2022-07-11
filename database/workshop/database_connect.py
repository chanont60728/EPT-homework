import mysql.connector
class blank_database_and_table():
    ##################################################
    ### ส่วนนี้เป็นการเชื่อมต่อชั่วคราวแล้วจะปิดแล้วเปิดใหม่ ###
    mydb = mysql.connector.connect(
        host = "localhost",
        user = "root",
        password = "",
    )
    print("เชื่อมต่อชั่วคราวเพื่อสร้าง database")

    # เป็นการเปิดให้ใช้คำสั่ง SQL ผ่าน py ได้ >>>> cursor.execute("ใส่คำสั่ง SQL")
    cursor = mydb.cursor()

    # สร้าง database (ใช้ครั้งเดียว)
    global database_name
    database_name = "HORPAK" # ถ้าจะแก้ชื่อ database ให้เปลี่ยนตรงนี้
    cursor.execute("CREATE DATABASE {}".format(database_name))
    print("สร้าง database ที่ชื่อ {} แล้ว".format(database_name))

    mydb.close()
    print("ปิดการเชื่อมต่อชั่วคราว")

    ##################################################
    ### หลังจากนี้จะเป็นการเชื่อมต่อเข้าไปในตัว database แล้ว ###

    # ส่วนนี้เป็นการสร้างตารางใน database (ใช้ครั้งเดียว) #
    def insert_table(self):

        # เพิ่มข้อมูลตารางและ column ของแต่ละตาราง ถ้าจะเพิ่มตารางหรือ column ให้มาเพิ่มตรงนี้#
        dict_of_SQL_command = {
        "client_detail" : "CREATE TABLE CLIENT_DETAIL(ClientID varchar(10) PRIMARY KEY not null,Firstname varchar(40) not null,Lastname varchar(40),E_mail varchar(40))",
        "horpak_detail" : "CREATE TABLE HORPAK(horpak_and_room_id varchar(10) PRIMARY KEY not null,horpak_name varchar(10) not null,room_number int not null,ClientID varchar(10) not null)",
        "reservation" : "CREATE TABLE RESERVATION(reserve_id varchar(10) PRIMARY KEY not null,horpak_and_room_id varchar(10) not null,ClientID varchar(10) not null,date_reserve date,date_check_in date not null)",
        "changing" : "CREATE TABLE CHANGING_ROOM(changing_id varchar(10) PRIMARY KEY not null,old_room_number int not null,new_room_number int not null,ClientID varchar(10) not null,date_changing date not null)",
        "invoice" : "CREATE TABLE INVOICE(horpak_and_room_id varchar(10) PRIMARY KEY not null,year_invoice int not null,month_invoice int not null,rent DECIMAL(7,2) not null,water DECIMAL(7,2) not null,Electric DECIMAL(7,2),cable DECIMAL(7,2),internet DECIMAL(7,2),fridge DECIMAL(7,2),laundry DECIMAL(7,2),damage DECIMAL(7,2),bedding DECIMAL(7,2),clean DECIMAL(7,2),fine DECIMAL(7,2))"
        }

        mydb = mysql.connector.connect(
            host = "localhost",
            user = "root",
            password = "",
            database = database_name 
        )
        print("เชื่อมต่อกับ database ที่ชื่อ {} แล้ว".format(database_name))

        # เป็นการเปิดให้ใช้คำสั่ง SQL ผ่าน py ได้ >>>> cursor.execute("ใส่คำสั่ง SQL")
        cursor = mydb.cursor()

        for key,value in dict_of_SQL_command.items():
            cursor.execute(value)
            print("สร้างตาราง {} แล้ว".format(key))
        
        mydb.close()
        print("ปิดการเชื่อมต่อแล้ว")


database_horpak = blank_database_and_table()
database_horpak.insert_table()


