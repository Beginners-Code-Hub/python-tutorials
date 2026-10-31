class Product:
    def __init__(self, name, stock):
        self.name = name
        self.stock = stock

    def restock(qty):  # forgot self
        self.stock += qty


rice = Product("Rice 5kg", 40)
rice.restock(5)
