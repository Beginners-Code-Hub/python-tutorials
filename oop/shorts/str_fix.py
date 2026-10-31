class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def __str__(self):
        return f"{self.name}: {self.stock} pcs"


rice = Product("Rice 5kg", 40)
print(rice)
