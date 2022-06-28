import math

list_of_city_position = []

class city_position():
    def __init__(self,name,lat=0,lon=0):
        self.name = name
        self.lat = lat
        self.lon = lon

    def distance(self,lat2,lon2):
        self.lon = math.radians(self.lon)
        lon2 = math.radians(lon2)
        self.lat = math.radians(self.lat)
        lat2 = math.radians(lat2)
        
        # Haversine formula
        dlon = lon2 - self.lon
        dlat = lat2 - self.lat
        a = math.sin(dlat / 2)**2 + math.cos(self.lat) * math.cos(lat2) * math.sin(dlon / 2)**2

        c = 2 * math.asin(math.sqrt(a))
        
        # Radius ของโลกหน่วยกิโลเมตร
        r = 6371
        
        return c*r

# เปลี่ยน link ตรงนี้ให้เป็น path ที่เก็บไฟล์ worldcitiespop.txt
file = open(r'C:\Users\chano\Desktop\python project\ชีท\EPT python part2\worldcitiespop.txt', 'r' , encoding="ISO-8859-1")
f = file.readlines()
del f[0]

for i in range(len(f)):
    f[i].replace("\n","")
    prepare_for_class = f[i].split(",")
    object_creation = city_position(prepare_for_class[1],float(prepare_for_class[-2]),float(prepare_for_class[-1]))
    list_of_city_position.append(object_creation)

input_city = input("ใส่ชื่อเมือง (City): ")
k = int(input("ใส่ระยะห่างเป็นตัวเลข: "))
check = True

for j in list_of_city_position:
    if j.name == input_city:
        check = True
        city_chosen = j
        break
    else:
        check = None

ans_list = []
if check == None:
    print("ไม่มีเมืองอยู่ใน world cities")
else:
    for p in list_of_city_position:
        if city_chosen.distance(p.lat,p.lon)<k:
            ans_list.append(p.name)

print("list ด้านล่างนี้เป็นเมืองที่มีระยะทางน้อยกว่า k")
print(ans_list)