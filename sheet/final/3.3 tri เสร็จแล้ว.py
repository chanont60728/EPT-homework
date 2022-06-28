def loveTri(n):
    ans_list = []
    elements = 1
    list_previous = [1]

    for i in range(n):
        sublist_to_answer = [elements]

        for j in range(i):
            sublist_to_answer.append(elements)
            sublist_to_answer[-1] = sublist_to_answer[j]+list_previous[j]
            
        ans_list.append(sublist_to_answer)
        list_previous = sublist_to_answer
        elements = list_previous[-1]

    return ans_list

n = int(input("ใส่ค่า n : "))
print(loveTri(n))