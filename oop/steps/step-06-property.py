class Product:
    def __init__(self, name, price, stock):
        self.name = name
        self.price = price  # goes through the setter below
        self.stock = stock

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value


rice = Product("Rice 5kg", 275.0, 40)
rice.price = 260.0
print("New price:", rice.price)

try:
    rice.price = -50
except ValueError as error:
    print("Error:", error)
