class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price
        self.stock = stock

    def sell(self, qty):
        if qty > self.stock:
            raise ValueError(f"Only {self.stock} left")
        self.stock -= qty

    def restock(self, qty):
        self.stock += qty

    def total_value(self):
        return self.price * self.stock


rice = Product("Rice 5kg", 275.0, 40)
rice.sell(3)
rice.restock(10)
print(rice.name, "stock:", rice.stock)
print("Value:", rice.total_value())

Product.sell(rice, 2)  # the same as rice.sell(2)
print(rice.name, "stock:", rice.stock)

try:
    rice.sell(100)
except ValueError as error:
    print("Error:", error)
