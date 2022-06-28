array = []
ans = []
while True:
    n = int(input("เพิ่มข้อมูลเข้า list (หากต้องการหยุดเพิ่มข้อมูลให้ใส่เลข 0): "))
    if n == 0:
        break
    else:
        array.append(n)
count_of_positive_number = 0
sum_of_negative_number = 0
for i in array:
    if i>0:
        count_of_positive_number = count_of_positive_number+1
    elif i<0:
        sum_of_negative_number = sum_of_negative_number+i
    else:
        break

ans.append(count_of_positive_number)
ans.append(sum_of_negative_number)
    
if ans[0] == 0 and ans[1] == 0 :
    print(array)
else:
    print(ans)
