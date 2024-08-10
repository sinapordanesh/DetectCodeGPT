def divisor_list(x):
    return tuple([i for i in range(1, x+1) if x % i == 0])

N = int(input())
t = [int(input()) for _ in range(N)]
div = divisor_list(max(t))
di = 0
for i in range(N):
    j = 0
    while div[j] < t[i]:
        j += 1
    else:
        di += div[j] - t[i]
print(di)
