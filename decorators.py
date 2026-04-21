# def deco(func):
#     def inner():
#         print('running inner()')
#     return inner

# @deco
# def target():
#     print('running target()')

# target()
# target

################################ Next block

# registry = []

# def register(func):
#     print(f'running register({func})')
#     registry.append(func)
#     return func

# @register
# def f1():
#     print('running f1()')

# @register
# def f2():
#     print('running f2()')

# def f3():
#     print('running f3()')

# def main():
#     print('running main()')
#     print('registry ->', registry)
#     f1()
#     f2()
#     f3()

# if __name__ == '__main__':
#     main()

################################ Next block

# from typing import Callable
# import time

# def param_timer_deco(func: Callable):
#     def wrapper(*args, **kwargs):
#         start = time.time()
#         res = func(*args, **kwargs)
#         end = time.time()
#         print(f"Total time is {end-start}")
#         return res 
#     return wrapper

# @param_timer_deco
# def my_func(sleep_time: int):
#     time.sleep(sleep_time)
#     return 123

# print(my_func(3))

################################ Next block


# def limit_calls(limit: int):
#     def wrapper(func: Callable):
#         def inner(*args, **kwargs):
#             nonlocal limit
#             if limit == 0:
#                 print("Your limit is done")
#                 return
            
#             res = func(*args, **kwargs)

#             limit -= 1
#             return res
#         return inner
#     return wrapper

# @limit_calls(2)
# def my_func():
#     return 112

# print(my_func())
# print(my_func())
# print(my_func())

################################ Next block

# from typing import Coroutine
# import asyncio

# def deco(coroutine: Coroutine):
#     async def wrapper(*args, **kwargs):
#         res = await coroutine(*args, **kwargs)
#         return res
#     return wrapper

# @deco
# async def my_async_func():
#     await asyncio.sleep(0.5)
#     return 1

# asyncio.run()

################################ Next block

# from functools import lru_cache
# import time

# @lru_cache
# def my_long_func():
#     time.sleep(3)
#     return 42

# print(my_long_func())
# print(my_long_func())
# print(my_long_func())

################################ Next block


