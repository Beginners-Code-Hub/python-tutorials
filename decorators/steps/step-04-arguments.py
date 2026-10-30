def announce(func):
    def wrapper(*args, **kwargs):
        print("Starting...")
        result = func(*args, **kwargs)
        print("Done!")
        return result
    return wrapper

@announce
def add(a, b):
    return a + b

print(add(2, 3))
