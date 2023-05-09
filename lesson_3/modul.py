def max1(a, b):
    if a>b:
        return a
    return b

def fib(n):
    if n in [1,2]:
        return 1
    return fib(n-1) + fib(n-2)