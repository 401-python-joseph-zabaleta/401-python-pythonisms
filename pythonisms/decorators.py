from functools import wraps

def proclaim(txt):
    return txt


def emphasize(func):
    @wraps(func)
    def wrapper(*args, **kwargs):

        return_val_from_undecorated_function = func(*args, **kwargs)

        emphasized = return_val_from_undecorated_function.upper() + "!!!"

        return emphasized

    return wrapper


def sarcastic(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        orig_val = func(*args, **kwargs)
        return f'{orig_val}{orig_val}'

    return wrapper


def reverse_letters(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        
        output = ''
        
        orig_val = func(*args, **kwargs)


        for char in range(len(orig_val) - 1, -1, -1):
            output += orig_val[char]
        
        return output
    
    return wrapper