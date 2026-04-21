import time
from typing import Callable
from functools import wraps

def retry(times: int, delay: float, exceptions: tuple[type[Exception], ...] = (Exception,)):
    def decorator(func: Callable):
        @wraps(func)
        def wrapper(*args, **kwargs):
            cnt = times
            while cnt > 0:
                cnt -= 1
                try:
                    res = func(*args, **kwargs)
                    return res
                except exceptions:
                        if cnt == 0:
                            raise 
                        time.sleep(delay)
        return wrapper
    return decorator

attempts = {"count": 0}

@retry(times=5, delay=1)
def flaky():
    attempts["count"] += 1
    print(f"  попытка #{attempts['count']}")
    if attempts["count"] < 3:
        raise ValueError("пока рано")
    return "успех!"

result = flaky()
print("результат:", result)

