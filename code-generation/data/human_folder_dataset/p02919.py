import sys
from heapq import heappush, heappop

read = sys.stdin.read
readline = sys.stdin.readline
readlines = sys.stdin.readlines
sys.setrecursionlimit(10 ** 9)
INF = 1 << 60
MOD = 1000000007


class BIT:
    def __init__(self, n):
        self.n = n
        self.data = [0] * (n + 1)
        self.step = pow(2, n.bit_length() - 1)

    def add(self, i, x=1):
        i += 1
        while i <= self.n:
            self.data[i] += x
            i += i & -i

    def get_sum(self, i):
        i += 1
        x = 0
        while i > 0:
            x += self.data[i]
            i -= i & -i
        return x

    # Return sum for [l, r)
    def get_sum_range(self, l, r):
        return self.get_sum(r - 1) - self.get_sum(l - 1)

    # Return the minimum i that satisfies a_0 + a_1 + ... + a_i >= x
    def lower_bound(self, x):
        if x <= 0:
            return 0
        i = 0
        k = self.step
        while k:
            if i + k <= self.n and self.data[i + k] < x:
                x -= self.data[i + k]
                i += k
            k >>= 1
        return i


def main():
    N, *P = map(int, read().split())

    index = [0] * (N + 1)
    for i, p in enumerate(P):
        index[p] = i

    bit = BIT(N)

    ans = 0
    for n in range(N, 0, -1):
        i = index[n]
        bit.add(i)
        x = bit.get_sum(i)

        left1 = left2 = -1
        right1 = right2 = N
        if x - 2 > 0:
            left2 = bit.lower_bound(x - 2)
        if x - 1 > 0:
            left1 = bit.lower_bound(x - 1)
        if x + 1 <= N - n + 1:
            right1 = bit.lower_bound(x + 1)
        if x + 2 <= N - n + 1:
            right2 = bit.lower_bound(x + 2)

        ans += ((left1 - left2) * (right1 - i) + (right2 - right1) * (i - left1)) * n

    print(ans)
    return


if __name__ == '__main__':
    main()
