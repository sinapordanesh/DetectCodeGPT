INF = float('inf')

def judge(src):
    x_max = INF
    x_min = -INF
    for i,(s1,s2) in enumerate(zip(src,src[1:])):
        if s1 == s2:
            return 'none'
        if i%2:
            s1,s2 = s2,s1
        if s1 != 'x' and s2 != 'x':
            if s1 < s2:
                return 'none'
            else:
                continue
        if s1 == 'x':
            if x_max <= s2:
                return 'none'
            x_min = max(x_min, s2 + 1)
        elif s2 == 'x':
            if s1 <= x_min:
                return 'none'
            x_max = min(x_max, s1 - 1)
        if x_max < x_min:
            return 'none'
    return x_max if x_max == x_min else 'ambiguous'

while True:
    N = int(input())
    if N == 0: break
    src = [INF] + list(map(lambda x:x if x=='x' else int(x), input().split())) + [INF if N%2 else -INF]
    print(judge(src))