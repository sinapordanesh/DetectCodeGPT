from functools import lru_cache


def DEBUG(*args): pass # print('@', *args)


@lru_cache(maxsize=None)
def pat(s, n):
    return ' '.join([s] * n)


DEBUG(pat('1', 3))


def removeAll(xs, s):
    while s in xs:
        xs.remove(s)
        xs.append('#')
    return xs


def lmap(f, s): return list(map(f, s))


digits = lmap(str, range(1, 10))

def main(n):
    data = '\n'.join(map(lambda x: input(), range(n)))
    score = 0
    DEBUG(data)
    while True:
        removed = False
        sum1 = sum(map(lambda x: 0 if x == '#' else int(x), data.split()))
        for d in digits:
            if pat(d, 3) in data:
                data = data.replace(pat(d, 5), pat('0', 5))
                data = data.replace(pat(d, 4), pat('0', 4))
                data = data.replace(pat(d, 3), pat('0', 3))
                removed = True
        if removed == False:
            break
        DEBUG(data)
        score += (sum1 - sum(map(lambda x: 0 if x == '#' else int(x), data.split())))
        data = zip(*map(lambda x: x.split(), data.split('\n')))
        data = map(lambda x: list(x[::-1]), data)
        data = map(lambda x: removeAll(x, '0'), data)
        data = lmap(lambda s: ' '.join(s), zip(*data))
        data = '\n'.join(data[::-1])
        DEBUG(data)
    DEBUG(data)
    print(score)

while True:
    n = int(input())
    if n == 0: break
    main(n)
