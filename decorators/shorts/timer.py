import time
from functools import wraps

def timer(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        t = time.perf_counter()
        result = func(*args, **kwargs)
        t = time.perf_counter() - t
        print(f"{func.__name__}: {t:.2f}s")
        return result
    return wrapper
