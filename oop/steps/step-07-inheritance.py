class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def __str__(self):
        return f"{self.name}: {self.stock} pcs at {self.price:.2f}"


class PerishableProduct(Product):
    def __init__(self, name, price, stock, days_left):
        super().__init__(name, price, stock)
        self.days_left = days_left

    def __str__(self):
        return super().__str__() + f" (expires in {self.days_left} days)"


rice = Product("Rice 5kg", 275.0, 40)
milk = PerishableProduct("Fresh milk", 95.0, 12, days_left=2)
print(rice)
print(milk)
print(isinstance(milk, Product))
