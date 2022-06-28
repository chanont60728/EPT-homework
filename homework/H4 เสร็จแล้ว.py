import random                                 #นำ module ชื่อ random
x = []                                        #สร้าง list เปล่าเก็บเข้าตัวแปร x
for i in range(0,10):                         #iterate เลข 0 ถึง 9 ผ่านตัวแปร i
    #x.append(int(input()))                   #เป็น comment ไม่ถูกประมวลผล
    x.append(random.randrange(50))            #ให้สุ่มค่าระหว่าง 0 ถึง 49 แล้วเพิ่มค่าเข้าไปใน list x ทำซ้ำจนกว่าจะจบ for loop i
print(x)                                      #แสดงค่า list x ออกมาทางหน้าจอ
for y in x:                                   #iterate ค่า y จาก list x
    if y>=10:                                 #ถ้า y มากกว่าหรือเท่ากับ 10
        print(y,end=" ")                      #แสดงค่า y ออกมาทางหน้าจอเว้นวรรค 1 ครั้งแล้วต่อด้วยค่า y เว้นวรรคอีก 1 ครั้งวนไปจนจบ for loop y
print()                                       #ขึ้นบรรทัดใหม่
########2#############
v = int(input("input V: "))                   #รับค่าเลขจำนวนเต็มจากแป้นพิมพ์ใส่เข้าตัวแปร v
have=False                                    #กำหนดให้ตัวแปร have เป็น False
for y in x:                                   #iterate ค่า y จาก list x
    if y==v:                                  #ถ้า y มีค่าเท่ากับ v
        have=True                             #กำหนดให้ตัวแปร have มีค่าเป็น True
if have:                                      #ถ้าตัวแปร have เท่ากับ True
    print(v," is in the array")               #ให้แสดงค่าของตัวแปร v ออกมาจากหน้าจอแล้วต่อด้วย is in the array
else:                                         #ถ้าเงื่อนไขใน if เป็น False
    print(v," is not in the array")           #ให้แสดงค่าของตัวแปร v ออกมาจากหน้าจอแล้วต่อด้วย is not in the array
########3#############
max2 = x[0]                                   #กำหนดให้ค่า max2 เป็นค่าใน list x ลำดับที่ 0
index = 0                                     #กำหนดให้ค่า index เป็นเท่ากับ 0
for y in range(0,len(x)):                     #iterate เลข 0 ถึงจำนวนข้อมูลใน list x ผ่านตัวแปร y
    if x[y]>max2:                             #ถ้าข้อมูลตำแหน่งที่ y ใน list x มีค่ามากกว่า max2
        max2=x[y]                             #ให้ตัวแปร max2 มีค่าเป็นข้อมูลตำแหน่งที่ y ใน list x
        index=y                               #ให้ตัวแปร index มีค่าเป็น y 

print("max2 = ",max2,"index = ",index)        #แสดงค่า max2= ค่าในตัวแปร max2 ต่อด้วย index= ค่าในตัวแปร index 
print("max = ",max(x))                        #แสดงค่า max= ข้อมูลใน list x ที่มีค่ามากที่สุด
########4#############
v = int(input("input v for search : "))       #รับค่าเลขจำนวนเต็มจากแป้นพิมพ์ใส่เข้าตัวแปร v
index = -1                                    #กำหนดให้ตัวแปร index มีค่าเป็น -1
for y in range(0,len(x)):                     #iterate เลข 0 ถึงจำนวนข้อมูลใน list x ผ่านตัวแปร y
    if x[y]==v:                               #ถ้าข้อมูลตำแหน่งที่ y ใน list x มีค่าเท่ากับ v
        index=y                               #ให้ตัวแปร index มีค่าเป็น y
        break                                 #แล้ว break ออกจาก for loop
if index == -1:                               #ถ้า index มีค่าเท่ากับ -1
    print(v," is not in list")                #ให้แสดงค่า v ออกมาทางหน้าจอและต่อด้วย is not in list
else:                                         #ถ้าเงื่อนไขใน if เป็น False
    x.pop(index)                              #ลบข้อมูลลำดับที่ระบุไว้ในตัวแปร index ออกไปจาก list x
    x.append(0)                               #และเติมหมายเลข 0 ต่อท้าย list x

    print(x)                                  #แสดงค่า list x ออกมาทางหน้าจอ
########5#############
v = int(input("input v for insert : "))       #รับค่าเลขจำนวนเต็มจากแป้นพิมพ์ใส่เข้าตัวแปร v
index = int(input("input index : "))          #รับค่าเลขจำนวนเต็มจากแป้นพิมพ์ใส่เข้าตัวแปร index

x.insert(index,v)                             #เพิ่มข้อมูล v เป็นลำดับที่ index เข้าไปใน list x
del x[len(x)-1]                               #ลบข้อมูลลำดับสุดท้ายใน list x 
print(x)                                      #แสดงค่า list x ออกมาทางหน้าจอ
########6#############
y=x.copy()                                    #copy list x แล้วเอาสำเนาไปเก็บเข้าตัวแปร y
y.sort()                                      #เรียงลำดับ list y จากน้อยไปมาก 
y.reverse()                                   #สลับตำแหน่งข้อมูลใน list y ให้กลายเป็นเรียงจากมากไปน้อย 
print(y)                                      #แสดง list y ออกมาทางหน้าจอ
########7#############
x=[]                                          #สร้าง list เปล่าเก็บเข้าตัวแปร x
for i in range(0,10):                         #iterate เลข 0 ถึง 9 ผ่านตัวแปร i
    #x.append(int(input()))                   #เป็น comment ไม่ถูกประมวลผล
    x.append(random.randrange(50))            #ให้สุ่มค่าระหว่าง 0 ถึง 49 แล้วเพิ่มค่าเข้าไปใน list x ทำซ้ำจนกว่าจะจบ for loop i

y=[]                                          #สร้าง list เปล่าเก็บเข้าตัวแปร y
for i in range(0,10):                         #iterate เลข 0 ถึง 9 ผ่านตัวแปร i
    #x.append(int(input()))                   #เป็น comment ไม่ถูกประมวลผล
    y.append(random.randrange(50))            #ให้สุ่มค่าระหว่าง 0 ถึง 49 แล้วเพิ่มค่าเข้าไปใน list y ทำซ้ำจนกว่าจะจบ for loop i

z=[]                                          #สร้าง list เปล่าเก็บไว้ในตัวแปร z
z.extend(x)                                   #เพิ่มข้อมูลทั้งหมดใน list x เข้าไปใน list z
z.extend(y)                                   #เพิ่มข้อมูลทั้งหมดใน list y เข้าไปใน list z
print(x)                                      #แสดง list x ออกมาทางหน้าจอ
print(y)                                      #แสดง list y ออกมาทางหน้าจอ
print(z)                                      #แสดง list z ออกมาทางหน้าจอ

x = [1,2,1,3,8,5,4,6,8,4,2,5,6,1,2,0,0,1,2]   #สร้าง list x เก็บข้อมูล 1,2,1,3,8,5,4,6,8,4,2,5,6,1,2,0,0,1,2
y = [-1,0,1]                                  #สร้าง list y เก็บข้อมูล -1,0,1
z = []                                        #สร้าง list เปล่าเก็บไว้ในตัวแปร z
for i in range(0,len(x)-len(y)):              #iterate เลข 0 ถึงจำนวนข้อมูลใน list x ลบจำนวนข้อมูลใน list y ผ่านตัวแปร i
    k=0                                       #กำหนดให้ตัวแปร k เป็น 0
    for j in range(0,len(y)):                 #iterate เลข 0 ถึงจำนวนข้อมูลใน list y ผ่านตัวแปร j
        k=k+y[j]*x[i+j]                       #กำหนดให้ตัวแปร k มีค่าเป็นข้อมูลใน list y ลำดับที่ j คูณกับข้อมูลใน list x ลำดับที่ i+j แล้วนำผลคูณไปบวกกับค่าในตัวแปร k ทำวนซ้ำไปจนกว่าจะหมด for loop j
    x.append(k)                               #ให้เพิ่มค่า k ที่คำนวณได้จาก for loop เข้าไปใน list x ทำซ้ำจนกว่าจะหมด for loop i
print(x)                                      #แสดงค่า list x ออกมาทางหน้าจอ
print(z)                                      #แสดงค่า list z ออกมาทางหน้าจอ
####################
import math                                   #นำเข้า module ชื่อ math เข้ามา
max_power = int(input("max_power "))          #รับค่าเลขจำนวนเต็มจากแป้นพิมพ์ใส่เข้าตัวแปร max_power
t = []                                        #สร้าง list เปล่าเก็บไว้ในตัวแปร t
while True:                                   #เมื่อเป็นจริงให้ทำซ้ำ (ซึ่งเป็นจริงตลอด)
    k=int(input("coefficient"))               #รับค่าเลขจำนวนเต็มจากแป้นพิมพ์ใส่เข้าตัวแปร k
    if k==-999:                               #ถ้าตัวแปร k มีค่าเท่ากับ -999
        break                                 #ให้ออกจาก while loop
    t.append(k)                               #ให้เพิ่มค่า k เข้าไปใน list t ทำซ้ำจนกว่าจะมีการใส่ค่า k เป็นเลข -999
s = []                                        #สร้าง list เปล่าเก็บไว้ในตัวแปร s
power_count = max_power                       #กำหนดให้มีตัวแปร power_count มีค่าเป็น max_power
for i in range(0,len(t)):                     #iterate เลข 0 ถึงจำนวนข้อมูลใน list t ผ่านตัวแปร i
    if power_count != -1:                     #ถ้าตัวแปร power_count มีค่าไม่เท่ากับ -1
        s.append(t[i]/(power_count+1))        #ให้นำข้อมูลลำดับที่ i ใน list t หารด้วยค่า power_count+1 แล้วนำผลหารใส่เข้าไปใน list s 
    else:                                     #ถ้าเงื่อนไขใน if เป็น False
        s.append(t[i])                        #ให้นำข้อมูลลำดับที่ i ใน list t ใส่เข้าไปใน list s
    power_count=power_count-1                 #ทบยอดค่า power_count ด้วย power_count-1 ทำซ้ำจนกว่าจะหมด for loop i

a = float(input("a"))                         #รับค่าเลขจำนวนทศนิยมจากแป้นพิมพ์ใส่เข้าตัวแปร a
b = float(input("b"))                         #รับค่าเลขจำนวนทศนิยมจากแป้นพิมพ์ใส่เข้าตัวแปร b
sum_a=0                                       #กำหนดให้ตัวแปร sum_a มีค่าเป็น 0
sum_b=0                                       #กำหนดให้ตัวแปร sum_b มีค่าเป็น 0
power_count = max_power                       #กำหนดให้มีตัวแปร power_count มีค่าเป็น max_power
for i in range(0,len(t)):                     #iterate เลข 0 ถึงจำนวนข้อมูลใน list t ผ่านตัวแปร i
    if power_count != -1:                     #ถ้าตัวแปร power_count มีค่าไม่เท่ากับ -1
        sum_a=sum_a+s[i]*pow(a,power_count+1) #ให้ค่า a ยกกำลังด้วย power_count+1 คูณกับข้อมูลในตำแหน่งที่ i ของ list s แล้วนำผลคูณมาบวกกับตัวแปร sum_a
        sum_b=sum_b+s[i]*pow(b,power_count+1) #ให้ค่า b ยกกำลังด้วย power_count+1 คูณกับข้อมูลในตำแหน่งที่ i ของ list s แล้วนำผลคูณมาบวกกับตัวแปร sum_b
    else:                                     #ถ้าเงื่อนไขใน if เป็น False
        sum_a=sum_a+s[i]*math.log(a)          #ให้ค่า log a คูณกับข้อมูลในตำแหน่งที่ i ของ list s แล้วนำผลคูณมาบวกกับตัวแปร sum_a
        sum_b=sum_b+s[i]*math.log(b)          #ให้ค่า log b คูณกับข้อมูลในตำแหน่งที่ i ของ list s แล้วนำผลคูณมาบวกกับตัวแปร sum_b
    power_count=power_count-1                 #ทบยอดค่า power_count ด้วย power_count-1 ทำซ้ำจนกว่าจะหมด for loop i

result = sum_b-sum_a                          #กำหนดตัวแปรชื่อ result ให้มีค่าเป็น sum_b-sum_a
print(result)                                 #แสดงค่าจากตัวแปร result ออกมาทางหน้าจอ
##########################
import math                                   #นำเข้า module ชื่อ math เข้ามา
def fac(n):                                   #สร้างฟังก์ชั่นชื่อ fac ให้มีพารามิเตอร์ที่ต้องใส่ค่าเข้าไปชื่อ n
    sum=1                                     #สร้างตัวแปร sum กำหนดให้มีค่าเป็น 1
    for i in range(1,n+1):                    #iterate เลข 1 ถึง n+1 ผ่านตัวแปร i
        sum*=i                                #ให้ทบยอดตัวแปร sum ด้วย sum คูณ i ทำซ้ำจนกว่าจะหมด for loop i
    return sum                                #คืนค่าผลลัพธ์กลับไปที่ตัวแปร sum
def power(a,n):                               #สร้างฟังก์ชั่นชื่อ power ให้มีพารามิเตอร์ที่ต้องใส่ค่าเข้าไปชื่อ a กับ n
    sum=1                                     #สร้างตัวแปร sum กำหนดให้มีค่าเป็น 1
    for i in range(1,n+1):                    #iterate เลข 1 ถึง n+1 ผ่านตัวแปร i
        sum*=a                                #ให้ทบยอดตัวแปร sum ด้วย sum คูณ a ทำซ้ำจนกว่าจะหมด for loop i
    return sum                                #คืนค่าผลลัพธ์กลับไปที่ตัวแปร sum
def sin(x):                                   #สร้างฟังก์ชั่นชื่อ sin ให้มีพารามิเตอร์ที่ต้องใส่ค่าเข้าไปชื่อ n
    sum=0                                     #สร้างตัวแปร sum กำหนดให้มีค่าเป็น 0
    for i in range(1,170,2):                  #iterate เลข 1 ถึง 170 ผ่านตัวแปร i (โดยให้การ iterate เพิ่มขึ้นทีละ 2 ขั้น)
        if i%4==1:                            #ถ้า i หารด้วย 4 แล้วเหลือเศษ 1
            sum+=power(x,i)/fac(i)            #ให้ใช้ผลลัพธ์จากฟังก์ชั่น power ที่ใส่ค่า x กับ i หารด้วยผลลัพธ์จากฟังก์ชั่น fac ที่ใส่ค่า i แล้วใช้ผลหารบวกเข้าไปในค่า sum
        else:                                 #ถ้าเงื่อนไขใน if เป็น False
            sum-=power(x,i)/fac(i)            #ให้ใช้ผลลัพธ์จากฟังก์ชั่น power ที่ใส่ค่า x กับ i หารด้วยผลลัพธ์จากฟังก์ชั่น fac ที่ใส่ค่า i แล้วใช้ผลหารลบออกจากค่า sum
        print(sum)                            #แสดงค่าจากตัวแปร sum ออกมาทางหน้าจอ
    return sum                                #คืนค่าผลลัพธ์กลับไปที่ตัวแปร sum
print(fac(5)," ",power(2,10)," ",sin(math.pi/2)," ",math.pi) #แสดงค่า ผลลัพธ์จากฟังก์ชั่น fac ที่ใส่ค่า 5 เว้นวรรค 1 ครั้งต่อด้วยผลลัพธ์จากฟังก์ชั่น power ที่ใส่ค่า 2 กับ 10 เว้นวรรค 1 ครั้งต่อด้วยผลลัพธ์จากฟังก์ชั่น sin ที่ใส่ค่า pi หาร 2 เว้นวรรค 1 ครั้งต่อด้วยค่า pi
###########################

    