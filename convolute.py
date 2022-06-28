x=[1,2,1,3,8,5,4,6,8,4,2,5,6,1,2,1,0,0,1,0]
y=[-1,0,1]
z = []
for i in range(0,len(x)-len(y)+1):
    k=0
    for j in range(0,len(y)):
        k=k+x[j+i]*y[j]
    z.append(k)
print(z)





