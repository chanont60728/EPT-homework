class Point():
    x = 0
    y = 0
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def getX(self):
        return self.x
    def getY(self):
        return self.y

    def setX(self,x):
        self.x = x
        print("ตั้งพิกัดใหม่ให้จุด x แล้ว")
    def setY(self,y):
        self.y = y
        print("ตั้งพิกัดใหม่ให้จุด y แล้ว")
    
    def distanceTo(self,p):
        return ((self.x-p.x)**2 + (self.y-p.y)**2)**(1/2)

    def getQuadrant(self):
        if self.x >= 0 and self.y >= 0 :
            return 1
        elif self.x < 0 and self.y >= 0 :
            return 2
        elif self.x < 0 and self.y < 0 :
            return 3
        else:
            return 4
    
    def equals(self,p):
        if self.x == p.x and self.y == p.y:
            return True
        else:
            return False
    
    def toString(self):
        print("ล่าสุดจุดนี้แสดงพิกัดที่ x=",self.x,"และแสดงพิกัดที่ y=",self.y)

#กำหนดพิกัดให้จุดนี้
x_of_thispoint = int(input("กำหนดค่า x ให้จุดนี้: "))
y_of_thispoint = int(input("กำหนดค่า y ให้จุดนี้: "))
this_point = Point(x_of_thispoint,y_of_thispoint)

#กำหนดพิกัดของจุด p
x_of_p = int(input("กำหนดค่า x ให้จุด p: "))
y_of_p = int(input("กำหนดค่า y ให้จุด p: "))
p = Point(x_of_p,y_of_p)

#เรียกใช้ฟังก์ชั่น getX
print("พิกัดของ x นี้คือ",this_point.getX())

#เรียกใช้ฟังก์ชั่น getY
print("พิกัดของ y นี้คือ",this_point.getY())

#เรียกใช้ฟังก์ชั่น setX
input_new_x = int(input("กำหนดค่า x ใหม่: "))
this_point.setX(input_new_x)

#เรียกใช้ฟังก์ชั่น setY
input_new_y = int(input("กำหนดค่า y ใหม่: "))
this_point.setY(input_new_y)

#เรียกใช้ฟังก์ชั่น getX ใหม่หลังเปลี่ยนค่า
print("พิกัดของ x นี้คือ",this_point.getX())

#เรียกใช้ฟังก์ชั่น getY ใหม่หลังเปลี่ยนค่า
print("พิกัดของ y นี้คือ",this_point.getY())

#เรียกใช้ฟังก์ชั่น distanceTo
print("ระยะทางสั้นที่สุดบนระนาบสองมิติระหว่างจุดนี้ถึงจุด p คือ ",this_point.distanceTo(p))

#เรียกใช้ฟังก์ชั่น getQuadrant
print("จุดนี้อยู่ใน Quadrant ที่",this_point.getQuadrant())

#เรียกใช้ฟังก์ชั่น equals
print("ผลการตรวจสอบว่าจุดนี้กับจุด p มีพิกัดอยู่ที่เดียวกันหรือไม่ = ",this_point.equals(p))

#เรียกใช้ฟังก์ขั่น toString
this_point.toString()
