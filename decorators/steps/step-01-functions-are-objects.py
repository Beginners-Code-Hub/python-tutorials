def greet(name):
    return f"Hello, {name}!"

say = greet          # no brackets: we pass the function itself
print(say("Ana"))

def call_twice(func, value):
    print(func(value))
    print(func(value))

call_twice(greet, "Ben")
