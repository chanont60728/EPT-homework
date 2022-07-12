class deck():
    dok = ["CLB","DIM","HRT","SPD"]
    dict_dok = {"CLB":1,"DIM":2,"HRT":3,"SPD":4}

    value_show = ["A","2","3","4","5","6","7","8","9","10","J","Q","K"]
    equal_value = [1,2,3,4,5,6,7,8,9,10,11,12,13] 
    dict_value_show = {}

    for p in range(len(value_show)):
        dict_value_show[value_show[p]] = equal_value[p]

    def show_all_deck(self):
        for i in self.dok:
            if self.dok.index(i)+1 == len(self.dok):
                for j in self.value_show:
                    if self.value_show.index(j)+1 == len(self.value_show):
                        print("({}, {})".format(i,j))
                    else:
                        print("({}, {})".format(i,j),end=" ")
            else:
                for j in self.value_show:
                    print("({}, {})".format(i,j),end=" ")

    def compare(self,get_tuple1:str,get_tuple2:str):
        if get_tuple1[1:4] == get_tuple2[1:4]:
            if get_tuple1[6:8] == "10" and get_tuple2[6:8] != "10":
                if self.dict_value_show[get_tuple1[6:8]] > self.dict_value_show[get_tuple2[6]]:
                    print(get_tuple1)
                else:
                    print(get_tuple2)

            elif get_tuple1[6:8] != "10" and get_tuple2[6:8] == "10":
                if self.dict_value_show[get_tuple1[6]] > self.dict_value_show[get_tuple2[6:8]]:
                    print(get_tuple1)
                else:
                    print(get_tuple2)

            else:
                if self.dict_value_show[get_tuple1[6]] > self.dict_value_show[get_tuple2[6]]:
                    print(get_tuple1)
                else:
                    print(get_tuple2)
        
        else:
            if self.dict_dok[get_tuple1[1:4]] > self.dict_dok[get_tuple2[1:4]]:
                print(get_tuple1)
            else:
                print(get_tuple2)


example = deck()
compare1 = input("")
compare2 = input("")
example.compare(compare1,compare2)
