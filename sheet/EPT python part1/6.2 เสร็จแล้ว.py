# เลือก BEAUTY
import matplotlib.pyplot as plt
from datetime import datetime

data = []
data_date = []

# เปลี่ยน path ตรงนี้ให้เป็นที่เดียวกับที่เก็บไฟล์ txt
with open(r"C:\Users\chano\Desktop\python project\ชีท\EPT python part1\BEAUTY.txt","r") as fd:
    for i in fd:
        i = i.strip("\n")
        i = float(i)
        data.append(i)

# เปลี่ยน path ตรงนี้ให้เป็นที่เดียวกับที่เก็บไฟล์ txt
with open(r"C:\Users\chano\Desktop\python project\ชีท\EPT python part1\BEAUTY date.txt","r") as fd:
    for i in fd:
        i = i.strip("\n")
        i = datetime.strptime(i,"%d-%b-%y")
        data_date.append(i)

# เนื่องจากในไฟล์ต้นฉบับแสดงราคาหุ้นจากท้ายไปต้น จึงต้อง reverse เพื่อให้ในกราฟแสดงจากหัวไปท้าย
data_date.reverse()
data.reverse()

average = []

for i in range(len(data)):
    sum = 0
    for j in range(i+1):
        sum = sum+data[j]
    average.append(sum/(i+1))

x = data_date
y = average
plt.title("BEAUTY STOCK MOVING AVERAGE PRICE PER DAY")
plt.plot(x,y)
plt.show()