class CoffeeShop:
    def __init__(self,billingMachine,cups,tables,sugar,milk,coffeeBeans):
        self.billingMachine=billingMachine
        self.cups=cups
        self.tables=tables
        self.sugar=sugar
        self.milk=milk
        self.coffeeBeans=coffeeBeans

    @staticmethod
    def bill(qty):
        print(15*qty)

c1=CoffeeShop(True,True,False,True,False,True)  
c1.bill(3)
CoffeeShop.bill(5)          