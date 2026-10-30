def announce(func):
    def wrapper():
        print("Starting...")
        func()
        print("Done!")
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(2, 3))
