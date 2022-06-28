def fac2(n):
    #base case (กรณีพื้นฐาน จะจบแล้ว)
    if n==1 or n==0:
        return 1
    #general case (กรณีทั่วไป ใช้วน)
    return n*fac2(n-1) #fac2 อยู่ในฟังก์ชั่นตัวเองด้วย หาก n ไม่ใช่ 1 หรือ 0 ก็มาวนในบรรทัดนี้

print(fac2(5))
    