n = input('choose a number')
if str(n) == str(n)[::-1] :
    print("yes")
    
else:
    print("no")
    

# ใส่ค่าเข้าไปในตัวแปร n ซึ่งอาจจะเป็นตัวอักษรหรือตัวเลขก็ได้แต่หลังจากนั้นตัวแปร n จะถูกเปลี่ยนเป็น string ในบรรทัดต่อไป
# str(n)[::-1] จะเป็นการ slice เข้าไปในแต่ละตัวอักษร <object_name>[<start_index>, <stop_index>, <step>] และ step ที่ -1 จะเป็นการสลับข้าง
# เช่น จาก 1234 จะกลายเป็น 4321 หรือ กขค จะกลายเป็น คขก
# ดังนั้นหากใส่ตัวเลขหรือตัวอักษรเข้าไปตัวเดียวจะทำให้ str(n) == str(n)[::-1] เป็นจริง
# และหากใส่ตัวเลข (รวมทั้งติดลบ ทศนิยม) หรือตัวอักษรเข้าไปมากกว่า 1 ตัวจะทำให้ str(n) == str(n)[::-1] เป็นเท็จ