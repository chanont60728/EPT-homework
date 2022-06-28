a = int(input())
b = int(input())
c = int(input())

if a>=0 and a<=2147483647 and b>=0 and b<=2147483647 and c>=0 and c<=2147483647:
    if (a+b+c)%10>=5:
        print((a+b+c)+(10-(a+b+c)%10))
    else:
        print((a+b+c)-((a+b+c)%10))

else:
    print("ใส่ค่าระหว่าง 0 ถึง 2147483647 เท่านั้น")