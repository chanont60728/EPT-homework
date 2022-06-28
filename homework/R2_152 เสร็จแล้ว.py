class Student():
    def __init__(self,name,surname,score):
        self.name = name
        self.surname = surname
        self.score = score
stu = []
for i in range(10):
    x = input("ใส่ชื่อ: ")
    y = input("ใส่นามสกุล: ")
    z = int(input("ใส่คะแนน: "))
    stu.append(Student(x,y,z))
    
mymax = stu[0]
for i in range(10):
    if mymax.score < stu[i].score:
        mymax = stu[i]
print(mymax.name)
print(mymax.surname)

