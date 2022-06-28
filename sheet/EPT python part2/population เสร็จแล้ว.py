## เปลี่ยน directory ให้เป็น path ที่เก็บไฟล์ world.csv
file = open(r'C:\Users\chano\Desktop\python project\ชีท\EPT python part2\world.csv', 'r' , encoding="ISO-8859-1")
f = file.readlines()

dict_of_population = {}

# ดูจากไฟล์แล้วผู้เรียนเข้าใจว่า จำนวนประชากรที่แบ่งตามเมืองมี 4079 บรรทัด
for i in range(4079):
    f[i] = f[i].replace('"', '')
    f[i] = f[i].replace('\n', '')
    prepare_for_dict = f[i].split(";")
    dict_of_population[prepare_for_dict[1]] = int(prepare_for_dict[-1])

number_of_pop = []

for value in dict_of_population.values():
    number_of_pop.append(value)

# เรียงลำดับจากน้อยไปมาก
number_of_pop.sort()

for k in number_of_pop:
    for key, value in dict_of_population.items():
            if k == value:
                print(key,"มีจำนวน",value,"คน")