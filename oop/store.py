"""Mini store inventory: the final code from the video."""


class Product:
    tax_rate = 0.12  # class attribute: shared by all products
    count = 0

    def __init__(self, name, price, stock):
        self.name = name
        self.price = price  # goes through the setter below
        self.stock = stock
        Product.count += 1

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        if value < 0:
            raise ValueError("Price cannot be negative")
        self._price = value

    def sell(self, qty):
        if qty > self.stock:
            raise ValueError(f"Only {self.stock} left")
        self.stock -= qty

    def restock(self, qty):
        self.stock += qty

    def total_value(self):
        return self.price * self.stock

    def price_with_tax(self):
        return round(self.price * (1 + self.tax_rate), 2)

    def needs_attention(self):
        return self.stock < 5

    def __str__(self):
        return f"{self.name}: {self.stock} pcs at {self.price:.2f}"


class PerishableProduct(Product):
    def __init__(self, name, price, stock, days_left):
        super().__init__(name, price, stock)
        self.days_left = days_left

    def needs_attention(self):
        return super().needs_attention() or self.days_left <= 3

    def __str__(self):
        return super().__str__() + f" (expires in {self.days_left} days)"


class Inventory:
    def __init__(self):
        self.products = []

    def add(self, product):
        self.products.append(product)

    def total_value(self):
        return sum(p.total_value() for p in self.products)

    def report(self):
        print("=== Inventory report ===")
        for p in self.products:
            flag = "!" if p.needs_attention() else " "
            print(f"{flag} {p}")
        print(f"Total value: {self.total_value():,.2f}")
