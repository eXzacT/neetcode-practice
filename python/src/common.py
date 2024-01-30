from collections import deque
from typing import Callable
from time import perf_counter
from functools import wraps


def consume(iter):
    deque(iter, maxlen=0)


def time_execution(executions: int = 10) -> Callable:
    def decorator(func: Callable) -> Callable:
        @wraps(func)
        def wrapper(*args, **kwargs):
            elapsed_time = 0
            return_val = None
            for _ in range(executions):
                start = perf_counter()
                return_val = func(*args, **kwargs)
                end = perf_counter()
                elapsed_time += end - start
            print(
                f"Elapsed time for {func.__name__.ljust(50,'.')}avg = {(elapsed_time/executions)*1000:.4f}ms of {executions} times.")
            return return_val
        return wrapper
    return decorator
