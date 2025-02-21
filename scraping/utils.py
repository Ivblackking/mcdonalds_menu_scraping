import time


def time_delta(func):
    def wrapper(*args, **kwargs):
        t1 = time.time()
        res = func(*args, **kwargs)
        t2 = time.time()
        print(f"{func.__name__} time delta: {t2-t1}")
        return res
    return wrapper