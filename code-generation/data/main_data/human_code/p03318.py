import math

def s(n):
    ret = 0

    while n > 0:
        ret += n % 10
        n = n // 10
        
    return ret

def snuke(n):
    candidate = []

    for d in range(int(math.log(n, 10)) + 2):
        x = n - (n % 10**d) + (10**d - 1)
        candidate.append(x)
    
    min_value = candidate[0] / s(candidate[0])
    ans = candidate[0]
    for c in candidate[1:]:
        tmp = c / s(c)
        if tmp < min_value:
            min_value = tmp
            ans = c
            
    return ans

K = int(input())

N = 0
for i in range(K):
    N = snuke(N + 1)
    print(N)
        