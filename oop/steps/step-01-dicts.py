# Without classes: each product is a dictionary
rice = {"name": "Rice 5kg", "price": 275.0, "stock": 40}
milk = {"name": "Fresh milk", "price": 95.0, "stock": 12}


def sell(product, qty):
    product["stock"] -= qty


sell(rice, 3)
print(rice["name"], "stock:", rice["stock"])

eggs = {"name": "Eggs", "price": 110.0, "qty": 30}  # typo!
sell(eggs, 2)
