import time

def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        time_spend = end_time - start_time
        print(f'{func.__name__} cost time: {time_spend}')
        return result
    return wrapper