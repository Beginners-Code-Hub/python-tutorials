class Product:
    tax_rate = 0.12  # class attribute: shared by all products
    count = 0

    def __init__(self, name, price, stock):
        self.name = name  # instance attributes: one per object
        self.price = price
        self.stock = stock
        Product.count += 1

    def price_with_tax(self):
        return round(self.price * (1 + self.tax_rate), 2)


rice = Product("Rice 5kg", 275.0, 40)
milk = Product("Fresh milk", 95.0, 12)
print("Products created:", Product.count)
print(rice.price_with_tax(), milk.price_with_tax())

Product.tax_rate = 0.10  # change it once, every product sees it
print(rice.price_with_tax(), milk.price_with_tax())
