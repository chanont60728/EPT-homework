sum0 = 1
i = 1

while i<=10000:
    sum0 = sum0*i
    i=i+1
sum_to_list_str = list(str(sum0))

new_list=[]
sum = 0
for a in sum_to_list_str:
    sum = sum+int(a)
print(sum)
