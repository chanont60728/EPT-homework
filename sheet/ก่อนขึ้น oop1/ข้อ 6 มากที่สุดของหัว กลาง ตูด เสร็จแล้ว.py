def Maxtriple(func_n):
    return max(func_n[0],func_n[(len(func_n)//2)],func_n[len(func_n)-1])
    
m = int(input("ใส่ขนาดของ list ให้เป็นเลขคี่และเป็นจำนวนเต็มบวก: "))
list_of_m=[]
if m%2==0:
    print("ใส่ขนาดของ list ให้เป็นเลขคี่เท่านั้น!!!")
elif m<0:
    print("ใส่ขนาดของ list ให้เป็นจำนวนเต็มบวกเท่านั้น!!!")
else:
    for i in range(m):
        n=int(input("ใส่ข้อมูลเข้า list: "))
        list_of_m.append(n)
        filled_list = list_of_m[:]
    ans = Maxtriple(filled_list)
    print(ans)
