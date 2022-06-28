n = int(input("ใส่ค่า n : "))
at_k = (n*2)-1
p = n

for k in range(1,at_k+1,2):
    j=p
    while j > 0:
        print("#",end="")
        j=j-1

    
    print("*"*k,end="")

    j=p
    while j > 0:
        print("#",end="")
        j=j-1

    print()
    p=p-1

p=0
for k in range(at_k,0,-2):
    j=0
    while j <= p:
        print("#",end="")
        j=j+1

    
    print("*"*k,end="")

    j=0
    while j <= p:
        print("#",end="")
        j=j+1

    print()
    p=p+1