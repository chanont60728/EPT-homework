#จากตัวอย่าง 100 
# 100 ถอดรูทจะได้ 10 ยกกำลัง 2 แปลว่าระหว่าง 1-9 จะไม่มีตัวไหนยกกำลัง 2 แล้วถึง 100 และตั้งแต่ 11-99 เมื่อยกกำลังสองแล้วมากกว่า 100 หมด

n=100
i = 2
while i*i<=n: #i ไม่ใช่ 1 ไม่ใช่ n ดังนั้นถ้า n หารด้วย i ลงตัวก็แปลว่ามีตัวอื่นนอกจาก 1 กับ n หารลงตัว และไม่ใช่จำนวนเฉพาะ
    if n%i==0:
        print("ไม่ใช่จำนวนเฉพาะ")
    i=i+1
print("เป็นจำนวนเฉพาะ")

