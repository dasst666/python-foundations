from typing import Callable
import time
import logging
from functools import wraps

logger = logging.getLogger(__name__)

def time_log(func: Callable):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        res = func(*args, **kwargs)
        end = time.perf_counter()
        logger.info("Function %s took %.6f seconds", func.__name__, end - start)
        return res
    return wrapper

class Timed:
    def __init__(self, func):
        self.func = func

    def __call__(self, *args, **kwargs):
        start = time.perf_counter()
        res = self.func(*args, **kwargs)
        end = time.perf_counter()
        logger.info("Function %s took %.6f seconds (Timed class)", self.func.__name__, end - start)
        return res
    
@Timed
def my_func_2(delay_time: float):
    time.sleep(delay_time)
    return "Function done"

@time_log
def my_func(delay_time: float):
    time.sleep(delay_time)
    return "Function done"

if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, format="%(asctime)s %(levelname)s %(message)s")
    print(my_func(2.5))
    print(my_func_2(2.5))

