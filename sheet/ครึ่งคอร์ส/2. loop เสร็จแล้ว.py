n = int(input())
mod_list = []
for i in range(1,n):
    if n%i==0:
        mod_list.append(i)

print(sum(mod_list))