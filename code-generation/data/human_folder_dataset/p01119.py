from bisect import bisect_left, bisect_right
while True:
    n, m = map(int, input().split())
    if n == m == 0:
        break
    a = list(map(int, input().split()))
    w = list(map(int, input().split()))
    Set = set()
    def go(i, weight):
        if i == m:
            Set.add(weight)
            return
        go(i + 1, weight)
        go(i + 1, weight + w[i])
        go(i + 1, weight - w[i])
    go(0, 0)
    ans = False
    for i in a:
        if i not in Set:
            if ans == False:
                ans = set(abs(s - i) for s in Set)
            else:
                ans = set(s for s in ans if i + s in Set or i - s in Set)
    if ans == False:
        print(0)
        continue
    elif len(ans) == 0:
        print(-1)
        continue
    else:
        print(min(ans))
