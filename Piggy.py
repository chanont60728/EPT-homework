class History():
    def __init__(self,id:int=0,date:str="NA",action:str="NA",who:str="NA",amount:float=0.00,currency:str="THB"):
        self.id = id
        self.date = date
        self.action = action
        self.who = who
        self.amount = amount
        self.currency = currency

class Piggy():
    index_of_id = 0
    def __init__(self,date_input:str):
        self.moneyTH = 0.00
        self.moneyUS = 0.00
        self.historyList = []
        Piggy.index_of_id = Piggy.index_of_id + 1
        history_to_list = History(id = Piggy.index_of_id,date=date_input,action="start",who="me",amount=0.00)
        self.historyList.append(history_to_list)
        print("Create Piggy Bank at",date_input)
    
    def setMoneyTH(self,get_THB:float):
        self.moneyTH = self.moneyTH+get_THB
        print("Set Piggy Bank money to","{:.2f}".format(self.moneyTH),"THB")
    
    def setMoneyUS(self,get_USD:float):
        self.moneyUS = self.moneyUS+get_USD
        print("Set Piggy Bank money to","{:.2f}".format(self.moneyUS),"USD")
    
    def getMoney(self):
        print("My Piggy Bank has","{:.2f}".format(self.moneyTH),"THB and","{:.2f}".format(self.moneyUS),"USD")
    
    def depositTH(self,money_deposit:float,deposit_date:str):
        self.setMoneyTH(money_deposit)
        Piggy.index_of_id = Piggy.index_of_id + 1
        depositTH_transaction = History(id = Piggy.index_of_id,date=deposit_date,action="deposit",who="me",amount=money_deposit,currency="THB")
        self.getMoney()
        self.historyList.append(depositTH_transaction)
    
    def depositUS(self,money_deposit:float,deposit_date:str):
        self.setMoneyUS(money_deposit)
        Piggy.index_of_id = Piggy.index_of_id + 1
        depositUS_transaction = History(id = Piggy.index_of_id,date=deposit_date,action="deposit",who="me",amount=money_deposit,currency="USD")
        self.getMoney()
        self.historyList.append(depositUS_transaction)
    
    def withdraw(self,THB_withdraw:float,exchange_rate:float,date_withdraw:str):
        if self.moneyTH + (self.moneyUS*exchange_rate) < THB_withdraw:
            print("Not enough, Now has","{:.2f}".format(self.moneyTH),"THB","{:.2f}".format(self.moneyUS),"USD")
        else:
            if self.moneyTH >= THB_withdraw:
                self.moneyTH = self.moneyTH - THB_withdraw
                if self.moneyTH - int(self.moneyTH) >= 0.75 and self.moneyTH - int(self.moneyTH) < 1:
                    self.moneyTH = int(self.moneyTH) + 0.75
                elif self.moneyTH - int(self.moneyTH) >= 0.50 and self.moneyTH - int(self.moneyTH)< 0.75:
                    self.moneyTH = int(self.moneyTH) + 0.50
                elif self.moneyTH - int(self.moneyTH) >= 0.25 and self.moneyTH - int(self.moneyTH)< 0.50:
                    self.moneyTH = int(self.moneyTH) + 0.25
                else:
                    self.moneyTH = int(self.moneyTH)
                Piggy.index_of_id = Piggy.index_of_id + 1

                if THB_withdraw - int(THB_withdraw) >= 0.75 and THB_withdraw - int(THB_withdraw) < 1:
                    THB_withdraw = int(THB_withdraw) + 1
                elif THB_withdraw - int(THB_withdraw) >= 0.50 and THB_withdraw - int(THB_withdraw)< 0.75:
                    THB_withdraw = int(THB_withdraw) + 0.75
                elif THB_withdraw - int(THB_withdraw) >= 0.25 and THB_withdraw - int(THB_withdraw)< 0.50:
                    THB_withdraw = int(THB_withdraw) + 0.50
                elif THB_withdraw - int(THB_withdraw) >= 0.01 and THB_withdraw - int(THB_withdraw)< 0.25:
                    THB_withdraw = int(THB_withdraw)+ 0.25
                else:
                    THB_withdraw = int(THB_withdraw)

                withdraw_transaction_THB = History(id = Piggy.index_of_id,date=date_withdraw,action="withdraw",who="me",amount=THB_withdraw,currency="THB")
                self.historyList.append(withdraw_transaction_THB)                
                self.setMoneyTH(0.00)
            
            else:
                remaining = THB_withdraw - self.moneyTH
                Piggy.index_of_id = Piggy.index_of_id + 1
                withdraw_transaction_THB = History(id = Piggy.index_of_id,date=date_withdraw,action="withdraw",who="me",amount=self.moneyTH,currency="THB")
                self.historyList.append(withdraw_transaction_THB)

                self.moneyTH = 0.00
                
                Piggy.index_of_id = Piggy.index_of_id + 1
                withdraw_transaction_USD = History(id = Piggy.index_of_id,date=date_withdraw,action="withdraw",who="me",amount=remaining/exchange_rate,currency="USD")
                self.historyList.append(withdraw_transaction_USD)

                self.moneyUS = self.moneyUS - (remaining/exchange_rate)
                self.setMoneyTH(0.00)
                self.setMoneyUS(0.00)

            self.getMoney()
            
        
    def showHistory(self):
        print("**History**")
        for i in self.historyList:
            print(str(i.id)+"\t"+i.date+"\t"+i.action+"\t"+i.who+"\t"+"{:.2f}".format(i.amount)+"\t"+i.currency)
    
    def oneYear(self):
        import datetime
        this_year_have_365_or_366 = 0
        end_of_Feb = 0

        year_Create_Piggy,month_Create_Piggy,date_Create_Piggy = int(self.historyList[0].date.split("-")[0]),int(self.historyList[0].date.split("-")[1]),int(self.historyList[0].date.split("-")[2])
        data_date = datetime.date(year_Create_Piggy,month_Create_Piggy,date_Create_Piggy)

        if year_Create_Piggy % 4 == 0: 
            this_year_have_365_or_366 = 366
            end_of_Feb = 29
        else:
            this_year_have_365_or_366 = 365
            end_of_Feb = 28            

        if year_Create_Piggy % 100 == 0:
            this_year_have_365_or_366 = 365
            end_of_Feb = 28

        if year_Create_Piggy % 400 == 0:
            this_year_have_365_or_366 = 365
            end_of_Feb = 28
        
        if (year_Create_Piggy + 1) % 400 ==0:
            this_year_have_365_or_366 = this_year_have_365_or_366 + 1
            end_of_Feb = 29
        
        # start iterate 1 year
        for i in range(1,this_year_have_365_or_366+1):

            ### dad birthday section ###
            if  data_date.month == 2 and int(data_date.strftime("%d")) == end_of_Feb :
                self.withdraw(1000.00,0,data_date.strftime("%Y-%m-%d"))

            ### mom birthday section ###
            if  data_date.month == 8 and int(data_date.strftime("%d")) == 10 :
                self.withdraw(1200.00,0,data_date.strftime("%Y-%m-%d"))

            # weekday() = 4 = Friday
            ### Friday 18.00 section###
            if data_date.weekday() == 4:
                self.depositTH(100.00,data_date.strftime("%Y-%m-%d"))

            ### dad giving section ###
            dad_giving = 0
            if (data_date.month == 1 and int(data_date.strftime("%d")) == 31) or \
            (data_date.month == 2 and int(data_date.strftime("%d")) == end_of_Feb) or \
            (data_date.month == 3 and int(data_date.strftime("%d")) == 31) or \
            (data_date.month == 4 and int(data_date.strftime("%d")) == 30) or \
            (data_date.month == 5 and int(data_date.strftime("%d")) == 31) or \
            (data_date.month == 6 and int(data_date.strftime("%d")) == 30) or \
            (data_date.month == 7 and int(data_date.strftime("%d")) == 31) or \
            (data_date.month == 8 and int(data_date.strftime("%d")) == 31) or \
            (data_date.month == 9 and int(data_date.strftime("%d")) == 30) or \
            (data_date.month == 10 and int(data_date.strftime("%d")) == 31) or \
            (data_date.month == 11 and int(data_date.strftime("%d")) == 30) or \
            (data_date.month == 12 and int(data_date.strftime("%d")) == 31):

                dad_giving = self.moneyTH*(3/100)
                if dad_giving - int(dad_giving) > 0.75 and dad_giving - int(dad_giving) <= 1:
                    dad_giving = int(dad_giving) + 1
                elif dad_giving - int(dad_giving) > 0.50 and dad_giving - int(dad_giving) <= 0.75:
                    dad_giving = int(dad_giving) + 0.75
                elif dad_giving - int(dad_giving) > 0.25 and dad_giving - int(dad_giving) <= 0.50:
                    dad_giving = int(dad_giving) + 0.50
                elif dad_giving - int(dad_giving) == 0:
                    dad_giving = int(dad_giving)
                else:
                    dad_giving = int(dad_giving) + 0.25

                self.setMoneyTH(dad_giving)
                Piggy.index_of_id = Piggy.index_of_id + 1
                dad_giving_transaction = History(id = Piggy.index_of_id,date=data_date.strftime("%Y-%m-%d"),action="deposit",who="dad",amount=dad_giving,currency="THB")
                self.historyList.append(dad_giving_transaction) 
            
            ### my birthday section ###
            if  data_date.month == 11 and int(data_date.strftime("%d")) == 11 :
                mom_giving = self.moneyTH*(10/100)
                if mom_giving - int(mom_giving) > 0.75 and mom_giving - int(mom_giving) <= 1:
                    mom_giving = int(mom_giving) + 1
                elif mom_giving - int(mom_giving) > 0.50 and mom_giving - int(mom_giving) <= 0.75:
                    mom_giving = int(mom_giving) + 0.75
                elif mom_giving - int(mom_giving) > 0.25 and mom_giving - int(mom_giving) <= 0.50:
                    mom_giving = int(mom_giving) + 0.50
                elif mom_giving - int(mom_giving) == 0:
                    mom_giving = int(mom_giving)
                else:
                    mom_giving = int(mom_giving) + 0.25
                
                self.setMoneyTH(mom_giving)
                Piggy.index_of_id = Piggy.index_of_id + 1
                mom_giving_transaction = History(id = Piggy.index_of_id,date=data_date.strftime("%Y-%m-%d"),action="deposit",who="mom",amount=mom_giving,currency="THB")
                self.historyList.append(mom_giving_transaction)

            data_date = data_date+datetime.timedelta(days=1)
        
        self.showHistory()