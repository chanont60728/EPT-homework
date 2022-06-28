import math
class Vector():
    def __init__(self):
        self.x = 0
        self.y = 0
    def add(self,v):
        result_add = Vector()
        result_add.x = self.x+v.x
        result_add.y = self.y+v.y
        return result_add
    def sub(self,v):
        result_sub = Vector()
        result_sub.x = self.x-v.x
        result_sub.y = self.y-v.y
        return result_sub
    def dot(self,v):
        result_dot = (self.x*v.x)+(self.y*v.y)    
        return result_dot
    def size(self):
        result_size = math.sqrt((self.x)**2 + (self.y)**2)
        return result_size
    def unit(self):
        result_unit = Vector()
        result_unit.x = (1/Vector.size(self))*self.x
        result_unit.y = (1/Vector.size(self))*self.y
        return result_unit

vector1 = Vector()
vector2 = Vector()
vector1.x = float(5.5)
vector1.y = float(10)
vector2.x = float(46)
vector2.y = float(2.6)

# เรียกใช้ method บวก
result_add = vector1.add(vector2)
print("ผลบวกค่า x เท่ากับ",result_add.x)
print("ผลบวกค่า y เท่ากับ",result_add.y)

# เรียกใช้ method ลบ
result_sub = vector1.sub(vector2)
print("ผลลบค่า x เท่ากับ",result_sub.x)
print("ผลลบค่า y เท่ากับ",result_sub.y)

# เรียกใช้ method dot
result_dot = vector1.dot(vector2)
print("ค่า dot เท่ากับ",result_dot)

# เรียกใช้ method size
result_size = vector1.size()
print("ค่า size เท่ากับ",result_size)

# เรียกใช้ method unit
result_unit = vector1.unit()
print("ค่า unit ของ x เท่ากับ",result_unit.x)
print("ค่า unit ของ y เท่ากับ",result_unit.y)