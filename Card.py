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

