list_of_student = []
i = 1
while i<=10:
    student_name = input("กรุณาใส่ชื่อนักเรียน: ")
    list_of_student.append(student_name)
    student_surname = input("กรุณาใส่นามสกุลนักเรียน: ")
    list_of_student.append(student_surname)
    score = int(input("กรุณาใส่คะแนนของนักเรียน: "))
    list_of_student.append(score)
    i+=1

list_of_score = []
for i in range(2,30,3):
    list_of_score.append(list_of_student[i])
mak = max(list_of_score)

for i in range(2,30,3):
    if list_of_student[i] == mak:
        print(list_of_student[i-2]+" "+list_of_student[i-1]+" ได้คะแนนมากที่สุด")