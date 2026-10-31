class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock


class PerishableProduct(Product):
    def __init__(self, name, stock, days_left):
        self.days_left = days_left  # forgot super().__init__()


milk = PerishableProduct("Fresh milk", 12, 2)
print(milk.name)
