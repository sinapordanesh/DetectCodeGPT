n = int(input())
count = 0

def prime(n):
    if n == 2:
        return True
    else:
        i = 2
        while i ** 2 <= n:
            if n % i == 0:
                return False
            i += 1
        return True
i = n
while not prime(i):
    i += 1
print(i)