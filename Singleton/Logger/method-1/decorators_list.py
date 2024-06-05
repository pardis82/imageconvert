from functools import wraps

def singleton(cls):
    instances = {}
    
    @wraps(cls)
    def wrapper(*args, **kwargs):
        if cls not in instances:
            instances[cls] = cls(*args, **kwargs)
            # print(f"Creating instance of {cls}")
        return instances[cls]
    
    return wrapper
