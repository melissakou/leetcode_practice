from time import time

def timer(func):
    def wrapper_function(*args, **kwargs):
        t0 = time()
        result = func(*args, **kwargs)
        t1 = time()
        print("Time elapsed: %fs" % (t1-t0))
        return result
    return wrapper_function