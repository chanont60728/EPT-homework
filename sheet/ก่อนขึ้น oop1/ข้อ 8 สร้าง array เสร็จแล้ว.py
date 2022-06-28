def FizzArray3(a,b):
    list_of_fizz = []
    for i in range(a,b):
        list_of_fizz.append(i)
    return list_of_fizz

start = int(input("ใส่เลข start: "))
end = int(input("ใส่เลข end: "))

if end>=start:
    print(FizzArray3(start,end))
else:
    print("กรุณาใส่ให้เลข start มากกว่าหรือเท่ากับเลข end เท่านั้น")
