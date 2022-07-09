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
        if (self.value == "3" or self.value == "4" or self.value == "5" or self.value == "6" or self.value == "7" or self.value == "8" or self.value == "9" or self.value == "10"): 
            if (c2.value == "3" or c2.value == "4" or c2.value == "5" or c2.value == "6" or c2.value == "7" or c2.value == "8" or c2.value == "9" or c2.value == "10"):
                self.value = int(self.value)
                c2.value = int(c2.value)
                if self.value < c2.value:
                    return self.value < c2.value
        #if (self.value == "A" or self.value == "K" or self.value == "Q" or self.value == "J") or (c2.value == "A" or c2.value == "K" or c2.value == "Q" or c2.value == "J"):
        #    return self.value < c2.value            
    
    def __str__(self):
        return "({value} {suit})".format(value=self.value,suit=self.suit)

