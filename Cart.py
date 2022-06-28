class Product():
    def __init__(self,id="NA",quantity=1,price=0.00):
        self.id = id
        self.quantity = quantity
        self.price = price

class Cart():
    def __init__(self,id:str,name:str,tel:str):
        self.id = id
        self.name = name
        self.tel = tel
        self.productList = []
        print("Create Cart ID",self.id)
    
    def setName(self,name_change:str):
        old_name = self.name
        self.name = name_change
        print("Cart ID",self.id,"change name",old_name,"to",self.name)

    def setTel(self,tel_change:str):
        old_tel = self.tel
        self.tel = tel_change
        print("Cart ID",self.id,"change tel",old_tel,"to",self.tel)
    
    def addProduct(self,more_product_to_Cart:str):
        extracted_ID = more_product_to_Cart.split(" ")[0]
        extracted_price = more_product_to_Cart.split(" ")[1]
        product_go_to_cart = Product(id=extracted_ID,price=extracted_price)

        found = 0
        for i in self.productList:
            if product_go_to_cart.id != i.id:
                pass
            else:
                i.quantity = i.quantity+1
                found = 1
                if float(i.price) < float(product_go_to_cart.price):
                    i.price = product_go_to_cart.price
                print("Product",i.id,i.quantity,i.price)

        if found == 0:
            self.productList.append(product_go_to_cart)
            print("Product",product_go_to_cart.id,product_go_to_cart.quantity,product_go_to_cart.price)

    def removeProduct(self,id_remove:str):
        mode = 0
        for i in self.productList:
            if i.id == id_remove:
                mode = 1
                if i.quantity == 1:
                    print("Product",i.id,0)
                    self.productList.remove(i)
                else:
                    i.quantity = i.quantity-1
                    print("Product",i.id,i.quantity)

        if mode == 0:
            print("Product ID was wrong")
    
    def calculatePrice(self,mode:int):
        global sum_total
        sum_total = 0
        for i in self.productList:
            sum_total = sum_total+(float(i.price)*float(i.quantity))
        
        if mode == 1:
            print("Calculate","Price","Total","{:.2f}".format(sum_total))
        
        elif mode == 2:
            decimal_remain = sum_total - int(sum_total)
            if  decimal_remain >= 0.75 and decimal_remain < 1:
                sum_total = int(sum_total)+0.75
            elif decimal_remain >= 0.50 and decimal_remain < 0.75:
                sum_total = int(sum_total)+0.50
            elif decimal_remain >= 0.25 and decimal_remain < 0.50:
                sum_total = int(sum_total)+0.25
            print("Calculate","Price","Total","{:.2f}".format(sum_total))
        return sum_total
    
    def checkout(self,payment_method:str,payment_amount:float):
        import operator
             
        print("Cart detail")
        print("Cart ID",self.id,"Name",self.name,"Tel",self.tel)
        sorted_list = sorted(self.productList,key=operator.attrgetter('id'))
        
        for i in sorted_list:
            print("Product",i.id,i.quantity,i.price)

        if payment_method == "card" or payment_method == "transfer":
            print("Total",self.calculatePrice(1),"Paid by",payment_method)
        
        elif payment_method == "cash":
            print("Total","{:.2f}".format(self.calculatePrice(2)),"Paid","{:.2f}".format(payment_amount),"Change","{:.2f}".format(payment_amount - sum_total))


        



        