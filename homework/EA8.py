G = 11.5e6
OD = 0.5
N = 8
k = 2.681829632240412
oldd = 0
while True:
    d = ((8*k*N*((OD-oldd)**3))/G)**(1/4)
    if abs(d - oldd) < 0.000001:
        break
    oldd = d
print(d)