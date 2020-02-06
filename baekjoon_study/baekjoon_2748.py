import functools
import sys

def clock(func):
    def clocked(*args):
        result = func(*args)
        return result
    return clocked


@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n-2) + fibonacci(n-1)

if __name__=='__main__':
    a = int(sys.stdin.readline())
    print(fibonacci(a))