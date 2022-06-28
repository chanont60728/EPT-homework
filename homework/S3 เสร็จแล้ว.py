string = input("ใส่ string เพื่อตรวจสอบ: ")
reversed_string = string[::-1]

if string == reversed_string:
    print("เป็น palindrome")
else:
    print("ไม่เป็น palindrome")