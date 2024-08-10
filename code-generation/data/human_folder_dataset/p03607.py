import sys
def IS(): return sys.stdin.readline().rstrip()
def II(): return int(IS())
from functools import partial, reduce
from collections import Counter


def f_chain(*args):
    return reduce(lambda x, f: f(x), args)

def main():
    n = II()
    aa = [II() for _ in range(n)]
    c_cnt = Counter(aa).values()
    f_chain(c_cnt,
            partial(map, lambda x: 1 if x%2==1 else 0),
            sum,
            print)

if __name__ == '__main__':
    main()