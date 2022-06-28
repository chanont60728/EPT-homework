for a in range(1,500):
    for b in range(1,500):
        if b>a:
            c = (a**2+b**2)**(1/2)
            if c == int(c) and c<500:
                print(a,b,c)