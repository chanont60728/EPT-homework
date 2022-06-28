def automorphic(a):
    list_of_square_a = list(str(a**2))
    list_of_a = list(str(a))

    for i in range(0,len(list_of_a)):
        if list_of_a[i] == list_of_square_a[-len(list_of_a)+i]:
            return "Automorphic"
        else:
            return "Not!!"


n = int(input())
print(automorphic(n))