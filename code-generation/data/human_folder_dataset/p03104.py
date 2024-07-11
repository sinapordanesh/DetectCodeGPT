import itertools
a, b = map(int, input().split())

def hoge(x: int):
    ans = []
    t = 1
    while x >= t:
        temp = t * (x//(t * 2)) + max(x%(t * 2) - (t - 1), 0)
        ans.append(temp)
        t *= 2
    return ans
ans=0
t=1
for i, j in itertools.zip_longest(hoge(b) , hoge(a-1), fillvalue = 0):
    if (i - j) % 2 == 1:
        ans += t
    t *= 2
print(ans)

