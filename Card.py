class Card():
    def __init__(self,value,suit):
        self.value = value
        self.suit = suit

    def Constructor(self,value:str,suit:str):
        self.value = value
        self.suit = suit
    
    def getScore(self):
        if self.value == "A":
            return 1 
        elif self.value == "J" or self.value == "Q" or self.value == "K":
            return 10
        else:
            return int(self.value) 
    
    def sum(self,test_case):
        return (self.getScore() + test_case.getScore())%10
    
    def __lt__(self,c2):
        suit_list = ["club", "diamond", "heart", "spade"]
        value_list = ["3","4","5","6","7","8","9","10","J","Q","K","A","2"]
        if self.value != c2.value:
            # value compare section #
            if value_list.index(self.value) < value_list.index(c2.value):
                return value_list.index(self.value) < value_list.index(c2.value)
        else:
            # suit compare section #
            if suit_list.index(self.suit) < suit_list.index(c2.suit):
                return self.suit < c2.suit  

    def __str__(self):
        return "({value} {suit})".format(value=self.value,suit=self.suit)
    
    def next1(self):
        value_and_suit_list = [
            ("3","club"),("3","diamond"),("3","heart"),("3","spade"),
            ("4","club"),("4","diamond"),("4","heart"),("4","spade"),
            ("5","club"),("5","diamond"),("5","heart"),("5","spade"),
            ("6","club"),("6","diamond"),("6","heart"),("6","spade"),
            ("7","club"),("7","diamond"),("7","heart"),("7","spade"),
            ("8","club"),("8","diamond"),("8","heart"),("8","spade"),
            ("9","club"),("9","diamond"),("9","heart"),("9","spade"),
            ("10","club"),("10","diamond"),("10","heart"),("10","spade"),
            ("J","club"),("J","diamond"),("J","heart"),("J","spade"),
            ("Q","club"),("Q","diamond"),("Q","heart"),("Q","spade"),
            ("K","club"),("K","diamond"),("K","heart"),("K","spade"),
            ("A","club"),("A","diamond"),("A","heart"),("A","spade"),
            ("2","club"),("2","diamond"),("2","heart"),("2","spade"),
        ]

        temp_tuple = (self.value,self.suit)
        
        if self.value == "2" and self.suit=="spade":
            ans_index = 0
        else:
            ans_index = value_and_suit_list.index(temp_tuple) + 1
        
        ans = Card(value_and_suit_list[ans_index][0],value_and_suit_list[ans_index][1])
        return ans
    
    def next2(self):
        ans_of_2 = Card(self.value,self.suit)
        ans_of_2 = ans_of_2.next1()
        self.value = ans_of_2.value
        self.suit = ans_of_2.suit

