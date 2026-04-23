# Iterator
class MyIterator:
    def __init__(self, start, end):
        self.start = start
        self.end = end

    def __iter__(self):
        return self
    
    def __next__(self):
        if self.start >= self.end:
            raise StopIteration
        else:
            self.start += 1
            return self.start - 1
        
numbers = MyIterator(0, 5)
for number in numbers:
    print(number)

# Generator
def my_generator(start, end):
    current = start
    while current < end:
        yield current
        current += 1

numbers = my_generator(0, 5)
for number in numbers:
    print(number)
# #################################################################
class FibIterator:
    def __init__(self, num):
        self.num = num
        self.a, self.b = 0, 1
        self.idx = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.idx < self.num:
            self.a, self.b = self.b, self.a + self.b
            self.idx += 1
            return self.a
        raise StopIteration()

fib = FibIterator(5)
for i in fib:
    print(i)

def fib_generator(num):
    a, b = 0, 1
    for _ in range(num):
        a, b = b, a + b
        yield a

for i in fib_generator(5):
    print(i)
# #################################################################
from itertools import islice

def chunked(iterable, size):
    it = iter(iterable)
    while True:
       chunk = list(islice(it, size))
       if not chunk:
           break
       yield chunk
        

for i in chunked([1, 2, 3, 4, 5, 6, 7], 3):
    print(i)

# #################################################################

def take(iterable, n):
    it = iter(iterable)
    for _ in range(n):
        try:
            yield next(it)
        except StopIteration:
            return

def take(iterable, n):
    for _, value in zip(range(n), iterable):
        yield value

result = list(take([1, 2], 5))
print(result)
# #################################################################

def drop(iterable, n):
    it = iter(iterable)
    yield from islice(it, n, None)
        

for i in drop([1, 2, 3, 4, 5, 6, 7], 3):
    print(i)
    