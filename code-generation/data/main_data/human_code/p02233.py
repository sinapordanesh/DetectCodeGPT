def memolize(f):
    cache = {}

    def helper(x):
        if x not in cache:
            cache[x] = f(x)
        return cache[x]
    return helper

@memolize
def fib(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1

    return fib(n - 1) + fib(n - 2)

n = int(input())
print(fib(n))

