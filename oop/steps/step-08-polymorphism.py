class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def needs_attention(self):
        return self.stock < 5


class PerishableProduct(Product):
    def __init__(self, name, price, stock, days_left):
        super().__init__(name, price, stock)
        self.days_left = days_left

    def needs_attention(self):
        return super().needs_attention() or self.days_left <= 3


products = [
    Product("Rice 5kg", 275.0, 40),
    Product("Coffee beans", 420.0, 3),
    PerishableProduct("Fresh milk", 95.0, 12, days_left=2),
    PerishableProduct("Bread", 65.0, 20, days_left=5),
]

for p in products:
    print(p.name, "->", p.needs_attention())
