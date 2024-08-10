n = int(input())
a = list(map(int, input().split()))

# 0 3 5 -1  0
# 0 3 5 11 12
#cum 0 3 8 14 15
# 0   5 11 12
# 0 3    7  8
# 0 3 5    10

# (cumi+1)-(cumi-1) - (i+1 - i-1)
# 8-0 - 5-0
# 14-3 - 7-3
# 2 6 8
# 3 2 5

a.insert(0,0)
a.append(0)
def cumulative_sum(collection):
    result = [0]
    for i in range(1, len(collection)):
        item = abs(collection[i] - collection[i-1])
        result.append(result[-1] + item)
    return result
cuma = cumulative_sum(a)

lp=cuma[-1]

for i in range(n):
    gap=abs(cuma[i+2]-cuma[i])-abs(a[i+2]-a[i])
    print(lp-gap, flush=True)
