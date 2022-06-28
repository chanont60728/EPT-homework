list_of_int = []
list_of_str = []
ans = []

def sorter():
    while True:
        n = int(input("ใส่ตัวเลขเข้ามาใน list หากต้องการหยุดให้ใส่เลข 9999 : ")) #ให้เป็นค่า int
        if n == 9999:
            break
        else:
            list_of_int.append(n)
        
    while True:
        m = input("ใส่ตัวอักษรหรือตัวเลขเข้ามาใน list หากต้องการหยุดให้ใส่คำว่า quit : ") #ให้เป็นค่า str
        if m == "quit":
            break    
        else:   
            list_of_str.append(m)

    ans.extend(sorted(list_of_int))
    ans.extend(sorted(list_of_str))
    return ans

print(sorter())