class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


rice = Product("Rice 5kg", 275.0, 40)
milk = Product("Fresh milk", 95.0, 12)

print(rice.name, rice.price, rice.stock)
print(milk.name, milk.price, milk.stock)
