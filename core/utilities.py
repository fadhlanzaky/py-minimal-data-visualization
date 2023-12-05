import functools
import inspect

def adjust_kwargs(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        func_args = inspect.signature(func)._parameters
        func_args = {k:kwargs[k] for k in func_args if k in kwargs.keys()}

        # Run function
        ret = func(*args, **func_args)

        return ret
    
    return wrapper