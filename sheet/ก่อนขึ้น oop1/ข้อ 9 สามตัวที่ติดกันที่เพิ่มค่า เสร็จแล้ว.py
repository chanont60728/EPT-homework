n = int(input())
list_of_num = []
ans = 0

if n>=0 and n<=500:
    for i in range(n):
        num_to_list = int(input())
        list_of_num.append(num_to_list)

    if len(list_of_num)<3:
        print(False)
    else:
        for j in range(len(list_of_num)-2):
            if list_of_num[j]<list_of_num[j+1] and list_of_num[j+1]<list_of_num[j+2]:
                ans = 1
                break
        if ans==1:
            print(True)
        else:
            print(False) 
else:
    print("ให้ใส่เฉพาะเลขระหว่าง 0 ถึง 500 เท่านั้น")

