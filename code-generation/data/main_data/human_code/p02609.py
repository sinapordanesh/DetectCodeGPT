import sys
sys.setrecursionlimit(10**6)
read = sys.stdin.read
#readlines = sys.stdin.readlines
from collections import defaultdict

def main():
    def from10to2(p):
        res = []
        while p:
            p, t = divmod(p, 2)
            res.append(str(t))
        return "".join(res[::-1])

    def from2to10(p):
        res = 0
        num2 = 1
        for c in p[::-1]:
            if c == '1':
                res += num2
            num2 *= 2
        return res

    def f(p):
        if p == 0:
            return 0
        elif d1[p] > 0:
            return d1[p]
        else:
            ppop = from10to2(p).count('1')
            p2 = p % ppop
            fp = f(p2) + 1
            d1[p] = fp
            return fp

    n = int(input())
    x = list(input())

    numof1 = x.count('1')
    bin2_p = [0] * n
    num2 = 1
    for i1 in range(1, n+1):
        bin2_p[-i1] = num2
        num2 = (num2 * 2) % (numof1 + 1)

    bin2_m = [0] * n
    num2 = 1
    if numof1 == 1:
        pass
    else:
        for i1 in range(1, n+1):
            bin2_m[-i1] = num2
            num2 = (num2 * 2) % (numof1 - 1)

    xas10 = from2to10(x)
    xas10_p = xas10 % (numof1 + 1)
    if numof1 == 1:
        xas10_m = 0
    else:
        xas10_m = xas10 % (numof1 - 1)
    d1 = defaultdict(int)
    d1[0] = 0
    for j1 in range(n):
        if x[j1] == '1':
            if numof1 == 1:
                print(0)
            else:
                t0 = xas10_m - bin2_m[j1]
                t0 = t0 % (numof1 - 1)
                if t0 == 0:
                    print(1)
                else:
                    print(f(t0) + 1)
        else:
            t0 = xas10_p + bin2_p[j1]
            t0 = t0 % (numof1 + 1)
            if t0 == 0:
                print(1)
            else:
                print(f(t0) + 1)

if __name__ == '__main__':
    main()
