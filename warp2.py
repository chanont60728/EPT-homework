warp_num_and_a_and_b = input("")
warp_num_and_a_and_b = [int(x) for x in warp_num_and_a_and_b.split(" ")]
warp_num = warp_num_and_a_and_b[0]
a = warp_num_and_a_and_b[1]
b = warp_num_and_a_and_b[2]
ans = "no"

current_position = a

list_of_a = []
list_of_b = []
for i in range(warp_num):
    get_input = input("")
    get_input = [int(x) for x in get_input.split(" ")]
    list_of_a.append(get_input[0])
    list_of_b.append(get_input[1])

while True:
    if current_position in list_of_a:
        index = list_of_a.index(current_position)
        current_position = list_of_b[index]
    else:
        break
    
    if current_position == b:
        ans = "yes"
        break
    if len(list_of_a) == 0 and len(list_of_b) == 0:
        break

print(ans)



