#!/usr/bin/env python3
import sys
def input(): return sys.stdin.readline().rstrip()

# ライブラリ参照https://atcoder.jp/contests/practice2/submissions/16580070


class SegmentTree:

    __slots__ = ["func", "e", "original_size", "n", "data"]

    def __init__(self, length_or_list, func=max, e=-10**18):
        self.func = func
        self.e = e
        if isinstance(length_or_list, int):
            self.original_size = length_or_list
            self.n = 1 << ((length_or_list - 1).bit_length())
            self.data = [self.e] * (self.n*2)
        else:
            self.original_size = len(length_or_list)
            self.n = 1 << ((self.original_size - 1).bit_length())
            self.data = [self.e] * self.n + length_or_list + \
                [self.e] * (self.n - self.original_size)
            for i in range(self.n-1, 0, -1):
                self.data[i] = self.func(self.data[2*i], self.data[2*i+1])

    def replace(self, index, value):
        index += self.n
        self.data[index] = value
        index //= 2
        while index > 0:
            self.data[index] = self.func(
                self.data[2*index], self.data[2*index+1])
            index //= 2

    def folded(self, l, r):
        left_folded = self.e
        right_folded = self.e
        l += self.n
        r += self.n
        while l < r:
            if l % 2:
                left_folded = self.func(left_folded, self.data[l])
                l += 1
            if r % 2:
                r -= 1
                right_folded = self.func(self.data[r], right_folded)
            l //= 2
            r //= 2
        return self.func(left_folded, right_folded)

    def all_folded(self):
        return self.data[1]

    def __getitem__(self, index):
        return self.data[self.n + index]

    def max_right(self, l, f):
        # assert f(self.e)
        if l >= self.original_size:
            return self.original_size
        l += self.n
        left_folded = self.e
        while True:
            # l //= l & -l
            while l % 2 == 0:
                l //= 2
            if not f(self.func(left_folded, self.data[l])):
                while l < self.n:
                    l *= 2
                    if f(self.func(left_folded, self.data[l])):
                        left_folded = self.func(left_folded, self.data[l])
                        l += 1
                return l - self.n
            left_folded = self.func(left_folded, self.data[l])
            l += 1
            if l == l & -l:
                break
        return self.original_size

    # 未verify
    def min_left(self, r, f):
        # assert f(self.e)
        if r == 0:
            return 0
        r += self.n
        right_folded = self.e
        while True:
            r //= r & -r
            if not f(self.func(self.data[r], right_folded)):
                while r < self.n:
                    r = 2 * r + 1
                    if f(self.func(self.data[r], right_folded)):
                        right_folded = self.func(self.data[r], right_folded)
                        r -= 1
                return r + 1 - self.n
            if r == r & -r:
                break
        return 0


def minindex(x, y):
    if x[0] <= y[0]:
        return x
    else:
        return y


def main():
    n, m = map(int, input().split())
    S = list(map(lambda x: 0 if x == '0' else 10**10, list(input())))
    roots = [10**10]*(n+1)
    for i in range(1, min(m+2, n+1)):
        if S[i] < 10**9:
            S[i] = 1
            roots[i] = 0
    S = [[s, i] for i, s in enumerate(S)]
    seg = SegmentTree(S, minindex, [10**12, 10**12])
    for i in range(m+1, n+1):
        if S[i][0] < 10**9:
            dist, masu = seg.folded(i-m, i)
            roots[i] = masu
            seg.replace(i, [dist+1, i])
    #print(seg.data[16:])
    #print(roots)
    if seg.folded(n, n+1)[0] > 10**9:
        print(-1)
    else:
        ans = []
        while n > 0:
            ans.append(n-roots[n])
            n = roots[n]
        print(*ans[::-1], sep=" ")


if __name__ == '__main__':
    main()