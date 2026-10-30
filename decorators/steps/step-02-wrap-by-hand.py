def announce(func):
    def wrapper():
        print("Starting...")
        func()
        print("Done!")
    return wrapper

def make_tea():
    print("Making tea")

make_tea = announce(make_tea)
make_tea()
