n = input("")
list_of_n = list(n)

if list_of_n[0]=="f" and list_of_n[len(list_of_n)-1]=="b":
    print("FizzBuzz")
elif list_of_n[0]=="f" and list_of_n[len(list_of_n)-1]!="b":
    print("Fizz")
elif list_of_n[0]!="f" and list_of_n[len(list_of_n)-1]=="b":
    print("Buzz")
else:
    print(n)