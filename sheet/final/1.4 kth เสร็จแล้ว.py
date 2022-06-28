def sumofDigitsSquared(n:int):
    n = str(n)
    n = list(n)
    n = [int(x) for x in n]

    sum = 0
    for i in n:
        sum = sum+i**2
    return ishappy(sum)

def ishappy(n:int):
    if n == 1:
        return True
    elif n == 4:
        return False
    else:
        return sumofDigitsSquared(n)

def kthHappy(n:int):
    kth_list = []
    
    for i in range(1,10000):
        if ishappy(i):
            kth_list.append(i)
    #สั่งพิมพ์บรรทัด print(kth_list) เพื่อดู list ของ kth_list ทั้งหมดได้
    #print(kth_list)
    return kth_list[n-1]

###### หมายเหตุสำคัญ : จากในชีทตัวอย่างสุดท้ายที่ระบุว่า kthHappy(13) returns 97 นั้น ผู้เรียนได้ทดลองดูแล้วไม่น่าจะถูกต้องเนื่องจากสาเหตุคือ ######
###### ในโจทย์ข้อถัดไปข้อที่ 1.5 Happy Ranks ได้ระบุไว้ในตัวอย่างคือ happyRank(97) == 19 ไม่ใช่ 13 ซึ่งในข้อนี้หากใส่ input เป็นเลข 19 จะได้คำตอบคือ 97 เท่ากันกับข้อ 1.5######
###### ในข้อนี้หากใส่หมายเลข 13 จะได้คำตอบเป็น 70 ซึ่งหากไล่ดูจากในชีทส่วนที่เป็น first few happy number จะได้เท่ากัน######
###### ใน first few happy number ตกหมายเลข 28 ไปทำให้ลำดับคลาดเคลื่อนไป ######

get_num = int(input("ใส่ตัวเลขลำดับเพื่อหา kth happy: "))
print(kthHappy(get_num))
