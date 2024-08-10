import collections
def resolve():
    n = int(input())
    s = [input() for _ in range(n)]
    c = collections.Counter(s)
    max_count = c.most_common()[0][1]
    ans = [i[0] for i in c.items() if i[1]==max_count]
    for i in sorted(ans): print(i)
resolve()