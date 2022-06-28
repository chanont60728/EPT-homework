# เปลี่ยน directory ตรงนี้ให้เป็น path ที่เก็บไฟล์ txt
f = open(r"C:\Users\chano\Desktop\python project\homework\riwords.txt",mode="r",encoding="UTF-8")
file = f.readlines()
data_use = []

# ดึงเฉพาะคำออกมา ซึ่งเริ่มตั้งแต่บรรทัดที่ 47
for i in range(47,len(file)):
    to_new_list = file[i].replace("\n","")
    data_use.append(to_new_list)

# จะแสดงผลลัพธ์เรียงตามลำดับไม้เอก ไม้โท ไม้ตรี ไม้จัตวา แยกเป็นแต่ละคำ
print("แต่ละคำจะมีไม้เอก ไม้โท ไม้ตรี ไม้จัตวา เรียงตามลำดับดังนี้")

for j in data_use:
    mai_ek = j.count("่")
    mai_to = j.count("้")
    mai_tri = j.count("๊")
    mai_jattawa = j.count("๋")
    print(j,":",mai_ek,mai_to,mai_tri,mai_jattawa)
