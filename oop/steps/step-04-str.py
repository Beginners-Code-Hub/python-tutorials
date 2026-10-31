class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: {self.stock} pcs at {self.price:.2f}"


rice = Product("Rice 5kg", 275.0, 40)
milk = Product("Fresh milk", 95.0, 12)
print(rice)
print(milk)
