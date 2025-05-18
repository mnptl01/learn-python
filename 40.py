class Order:
    def __init__(self, item, price):
        self.item = item
        self.price = price

    def __gt__(self, ordr2):
        return self.price > ordr2.price 

ordr1 = Order("brush", 7)
ordr2 = Order("mop", 20)
print(ordr1 > ordr2)