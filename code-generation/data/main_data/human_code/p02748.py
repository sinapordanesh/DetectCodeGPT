#!/usr/bin/env python3
import sys


def solve(A: int, B: int, M: int, a: "List[int]", b: "List[int]", x: "List[int]", y: "List[int]", c: "List[int]"):
    ans = min(a) + min(b)
    for i in range(M):
        xi = x[i]
        yi = y[i]
        ci = c[i]
        t = a[xi-1] + b[yi-1] - ci
        if ans >= t:
            ans = t
    print(ans)
    return


# Generated by 1.1.7.1 https://github.com/kyuridenamida/atcoder-tools  (tips: You use the default template now. You can remove this line by using your custom template)
def main():
    def iterate_tokens():
        for line in sys.stdin:
            for word in line.split():
                yield word
    tokens = iterate_tokens()
    A = int(next(tokens))  # type: int
    B = int(next(tokens))  # type: int
    M = int(next(tokens))  # type: int
    a = [int(next(tokens)) for _ in range(A)]  # type: "List[int]"
    b = [int(next(tokens)) for _ in range(B)]  # type: "List[int]"
    x = [int()] * (M)  # type: "List[int]"
    y = [int()] * (M)  # type: "List[int]"
    c = [int()] * (M)  # type: "List[int]"
    for i in range(M):
        x[i] = int(next(tokens))
        y[i] = int(next(tokens))
        c[i] = int(next(tokens))
    solve(A, B, M, a, b, x, y, c)

if __name__ == '__main__':
    main()
