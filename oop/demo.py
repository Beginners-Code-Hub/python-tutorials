from store import Inventory, PerishableProduct, Product

shop = Inventory()
shop.add(Product("Rice 5kg", 275.0, 40))
shop.add(Product("Coffee beans", 420.0, 3))
shop.add(PerishableProduct("Fresh milk", 95.0, 12, days_left=2))
shop.add(PerishableProduct("Bread", 65.0, 20, days_left=5))

shop.products[0].sell(5)
shop.products[1].restock(1)
shop.report()
