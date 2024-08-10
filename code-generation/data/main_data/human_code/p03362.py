import math

def is_prime(n):
    if n == 1: return False

    for k in range(2, int(math.sqrt(n)) + 1):
        if n % k == 0:
            return False

    return True


N = int(input())

i = 1
ans = [2]
while True:
    num = 2 + 5 * i
    if is_prime(num):
        ans.append(num)
    if len(ans) == N:
        print(*ans)
        exit()
    i += 1