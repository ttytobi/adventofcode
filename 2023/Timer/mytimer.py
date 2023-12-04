from time import time

def performance(fn):
    def wrapper(*args, **kwargs):
        t1 = time()
        result = fn(*args, **kwargs)
        t2 = time()
        print(f'Function "{fn.__name__}" took {t2-t1}s to complete')
        return result
    return wrapper