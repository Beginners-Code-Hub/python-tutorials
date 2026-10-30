from functools import wraps

def retry(times):
    def decorator(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            for attempt in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except Exception as error:
                    print(f"Attempt {attempt} failed: {error}")
                    if attempt == times:
                        raise
        return wrapper
    return decorator

calls = 0

@retry(times=3)
def flaky_connect():
    global calls
    calls += 1
    if calls < 3:
        raise ConnectionError("server busy")
    return "Connected!"

print(flaky_connect())
