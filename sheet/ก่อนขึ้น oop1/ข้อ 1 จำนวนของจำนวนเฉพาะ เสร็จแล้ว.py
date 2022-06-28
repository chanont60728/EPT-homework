n = int(input())
m = int(input())
count = []
j = 1

if n>=0 and n<=2147483647 and m>=0 and m<=2147483647 :
    for i in range(n,m+1):
        for j in range(2,i):
            if i%j == 0:
                break
        else:
            count.append(i)
    if n ==1:
        print(len(count)-1)
    elif n ==0:
        print(len(count)-2)
    else:
        print(len(count))
else:
    print("ใส่ค่าระหว่าง 0 ถึง 2147483647 เท่านั้น")