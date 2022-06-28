def large(a,b):
    return a if a>b else b
def large3(a,b,c):
    m = a
    m = large(m,b)
    m = large(m,c)
    return m
x = int(input())
y = int(input())
z = int(input())
q=large3(x,y,z)
print(q)