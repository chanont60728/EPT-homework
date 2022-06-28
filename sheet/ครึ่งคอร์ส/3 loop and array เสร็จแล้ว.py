n = int(input())

def mahamit(a):
    mod_list = []
    for i in range(1,a):
        if a%i==0:
            mod_list.append(i)
    return sum(mod_list)

ans=[]
for i in range(1,n+1):
    klom1 = mahamit(i)
    klom2 = mahamit(klom1)
    if klom2==i and klom2!=klom1:
        ans.append(klom2)

for j in ans:
    print(j)
