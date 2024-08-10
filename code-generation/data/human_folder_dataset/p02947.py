import collections
def resolve():
    n = int(input())
    words = []
    for _ in range(n):
        words.append(str(sorted(list(input()))))
    a = collections.Counter(words)
    ans = 0
    for i in a.values():
        ans += i*(i-1)//2
    print(ans)
resolve()