import math
n = int(input())
ans=0
i=1
if n>=0 and n<=2147483647:
    while i<=n:
        ans = ans+(1/(i**2))
        i=i+1

else:
    print("ใส่ค่าระหว่าง 0 ถึง 2147483647 เท่านั้น")


print(math.sqrt(ans))
