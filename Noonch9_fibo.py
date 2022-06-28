import numpy

n_and_k = input("")
n = int(n_and_k.split(" ")[0])
k = int(n_and_k.split(" ")[1])

m = [[1,1],[1,0]]
f = m

for i in range(1,n):
    m = numpy.dot(m,f)

ans = m[0][0] + m[1][1]
print(m)
print(ans%k)
