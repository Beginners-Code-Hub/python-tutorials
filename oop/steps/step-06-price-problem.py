class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def total_value(self):
        return self.price * self.stock


rice = Product("Rice 5kg", 275.0, 40)
rice.price = -50  # nothing stops this
print("Value:", rice.total_value())
