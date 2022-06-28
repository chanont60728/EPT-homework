n = int(input("ใส่จำนวนเต็มบวกเท่านั้น: ")) #โจทย์ให้ใส่ number คือจำนวนดังนั้นจึงต้องไม่มีเลขศูนย์นำหน้า

if n<=0:
    print("ใส่จำนวนเต็มบวกเท่านั้น")
else:
    list_of_n_int = []
    list_of_n_str = list(str(n))

    for i in list_of_n_str:
        list_of_n_int.append(int(i))
    
    mode = True

    j = 1
    while j<=len(list_of_n_int)-1:
        if list_of_n_int[j-1] > list_of_n_int[j]:
            mode = False
            break
        j=j+1
    print(mode)
    
