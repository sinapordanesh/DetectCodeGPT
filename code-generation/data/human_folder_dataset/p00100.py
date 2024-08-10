def parse(i):
    l = input().strip().split()
    return ((i, l[0]), int(l[1]) * int(l[2]))


n = int(input())

while n:
    ss, d = [parse(_) for _ in range(n)], {}

    for s in ss:
        k = s[0][1]
        d[k] = (d[k][0], d[k][1] + s[1]) if k in d else s

    d = [v[0] for v in d.values() if v[1] >= 1000000]

    if d:
        print('\n'.join(k[1] for k in sorted(d)))
    else:
        print('NA')

    n = int(input())