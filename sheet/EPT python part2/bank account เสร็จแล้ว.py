class Account():
    def __init__(self,id:int=-999,name:str="DUMMY",password:str="DUMMY",balance:float=0.00):
        self.id = id
        self.name = name
        self.password = password
        self.balance = balance
        print("เปิดบัญชีหมายเลข",self.id,"ชื่อ",self.name,"และจำนวนเงินเริ่มต้น",self.balance)
    
    ## ส่วนของการฝากเงิน ##
    def deposit(self,check_password:str,amount_deposit:float):
        if check_password != self.password:
            print("password ไม่ถูกต้อง ห้ามทำรายการ !!!")
        else:
            self.balance = self.balance + amount_deposit
            print("ฝากเงินจำนวน",amount_deposit,"บาท เข้าบัญชีหมายเลข",self.id,"ชื่อ",self.name,"รวมแล้วมีจำนวน",self.balance)
    
    ## ส่วนของการถอนเงิน ##
    def withdraw(self,check_password:str,amount_withdraw:float):
        if check_password != self.password:
            print("password ไม่ถูกต้อง ห้ามทำรายการ !!!")
        else:
            if self.balance < amount_withdraw:
                print("เงินไม่พอ ไม่ให้ถอน!!!")
            else:
                self.balance = self.balance - amount_withdraw
                print("ถอนเงินจำนวน",amount_withdraw,"บาท ออกจากบัญชีหมายเลข",self.id,"ชื่อ",self.name,"เหลือ",self.balance)
    
    ## ส่วนของการเรียกดู ##
    def report(self,check_password:str):
        if check_password != self.password:
            print("password ไม่ถูกต้อง ไม่ให้ดู !!!")
        else:
            print("บัญชีหมายเลข",self.id,"ชื่อ",self.name,"มีเงินอยู่",self.balance)

list_of_account = []
account_id = 0

# เปิดบัญชี 10 คนพร้อมกัน
for i in range(10): 
    get_name = input("ใส่ชื่อผู้เปิดบัญชี: ")
    get_password = input("ใส่รหัสผ่าน: ")
    get_amount = float(input("ใส่จำนวนเงินฝากเริ่มต้น: "))
    account_id = account_id+1
    open_account = Account(id=account_id , name=get_name , password=get_password , balance=get_amount)
    list_of_account.append(open_account)

while True:
    x = 0
    mode = int(input("กด 1 เพื่อฝากเงินหรือกด 2 เพื่อถอนเงินหรือกด 3 เพื่อดู statement หรือกด -1 เพื่อออกจากโปรแกรม: "))

    ## ส่วนของการฝากเงิน ##
    if mode == 1: 
        get_id = int(input("ใส่เลขบัญชีธนาคาร: "))
        get_password = input("ใส่รหัสผ่าน: ")
        money_deposit = float(input("ใส่จำนวนเงินที่ต้องการฝาก: "))
        
        for j in range(10): 
            if get_id == list_of_account[j].id: 
                list_of_account[j].deposit(check_password=get_password,amount_deposit=money_deposit)
                x = 1
            else:
                pass
        
        if x == 0:
            print("ไม่มีหมายเลขบัญชีนี้อยู่ในระบบ")

    ## ส่วนของการถอนเงิน ##
    elif mode == 2:
        get_id = int(input("ใส่เลขบัญชีธนาคาร: "))
        get_password = input("ใส่รหัสผ่าน: ")
        money_withdraw = float(input("ใส่จำนวนเงินที่ต้องการถอน: "))

        for j in range(10): 
            if get_id == list_of_account[j].id: 
                list_of_account[j].withdraw(check_password=get_password,amount_withdraw=money_withdraw)
                x = 1
            else:
                pass
        
        if x == 0:
            print("ไม่มีหมายเลขบัญชีนี้อยู่ในระบบ")

    ## ส่วนของการดูรายงาน ##
    elif mode == 3:
        get_id = int(input("ใส่เลขบัญชีธนาคาร: "))
        get_password = input("ใส่รหัสผ่าน: ")

        for j in range(10): 
            if get_id == list_of_account[j].id:
                list_of_account[j].report(check_password=get_password)
                x = 1
            else:
                pass

        if x == 0:
            print("ไม่มีหมายเลขบัญชีนี้อยู่ในระบบ")

    elif mode == -1:
        print("ออกจากโปรแกรมแล้ว")
        break

    else:
        print("กดเลขตามที่กำหนดเท่านั้น")
