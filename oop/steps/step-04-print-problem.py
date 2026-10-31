class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock


rice = Product("Rice 5kg", 275.0, 40)
print(rice)
