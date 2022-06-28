# เปลี่ยน link ตรงนี้ให้เป็น path ที่เก็บไฟล์ test_virus.dll
file = open(r'C:\Users\chano\Desktop\python project\ชีท\EPT python part2\test_virus.dll', "rb")

byte = file.read(1)
i = 1
while byte:
    print(byte.hex(),"อยู่ลำดับที่",i)
    byte = file.read(1)
    i=i+1
file.close()

print("sequence ของ virus อยู่ในลำดับที่ 101 ถึง 116")

