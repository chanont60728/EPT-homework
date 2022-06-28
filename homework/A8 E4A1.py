a = int(input())
b = int(input())
c = int(input())
if a > 13:
    if b != 6:
        print("A")
    else:
        if c <= 7:
            print("B")
        else:
            print("C")
else:
    if b <= 16:
        print("D")
    else:
        if c > 6:
            print("E")
        else:
            print("F")
