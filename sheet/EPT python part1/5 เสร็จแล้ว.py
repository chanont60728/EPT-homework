while True:
    total_sales = int(input("Please input total sales: "))
    if total_sales < 0:
        print("exit")
        break
    elif total_sales < 10000:
        print(0)
    elif total_sales >= 10000 and total_sales < 25000:
        print(total_sales*(7/100))
    else:
        print(total_sales*(10/100))