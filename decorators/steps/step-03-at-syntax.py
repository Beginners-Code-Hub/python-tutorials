def announce(func):
    def wrapper():
        print("Starting...")
        func()
        print("Done!")
    return wrapper

@announce
def make_tea():
    print("Making tea")

make_tea()
