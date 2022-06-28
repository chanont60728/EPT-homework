import statistics
list_of_n = []
for i in range(10):
    n=float(input())
    list_of_n.append(n)


print(statistics.mean(list_of_n))
print(statistics.pvariance(list_of_n))