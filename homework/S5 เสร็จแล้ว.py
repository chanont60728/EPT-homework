string = input("ใส่ข้อความเพื่อหาตัว a: ")
count = 0
for i in string:
    if i == "a":
        count=count+1
print("มีตัว a เท่ากับ",count)