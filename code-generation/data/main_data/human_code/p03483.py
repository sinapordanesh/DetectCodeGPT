from collections import Counter


class fenwick_tree(object):
    def __init__(self, n):
        self.n = n
        self.data = [0] * n

    def __sum(self, r):
        s = 0
        while r > 0:
            s += self.data[r - 1]
            r -= r & -r
        return s

    def add(self, p, x):
        """ a[p] += xを行う"""
        assert 0 <= p and p < self.n
        p += 1
        while p <= self.n:
            self.data[p - 1] += x
            p += p & -p

    def sum(self, l, r):
        """a[l] + a[l+1] + .. + a[r-1]を返す"""
        assert 0 <= l and l <= r and r <= self.n
        return self.__sum(r) - self.__sum(l)


def calc_inversion(arr):
    N = len(arr)
    bit = fenwick_tree(N)
    atoi = {a: i for i, a in enumerate(arr)}
    res = 0
    for a in reversed(range(N)):
        i = atoi[a]
        res += bit.sum(0, i)
        bit.add(i, 1)
    return res


def calc_inv(arr):
    N = len(set(arr))
    atoi = {a: i for i, a in enumerate(sorted(set(arr)))}
    bit = fenwick_tree(N)
    res = 0
    for i, a in enumerate(arr):
        res += i - bit.sum(0, atoi[a] + 1)
        bit.add(atoi[a], 1)
    return res


def main():
    S = input()
    N = len(S)
    C = Counter(S)

    odd = 0
    mid = ""
    for k, v in C.items():
        if v & 1:
            odd += 1
            mid = k

    if N % 2 == 0:  # 偶数
        if odd:
            return -1
        half = {k: v // 2 for k, v in C.items()}
        cnt = {k: 0 for k in C.keys()}
        label = []
        left = []
        right = []
        for i, s in enumerate(S):
            if cnt[s] < half[s]:
                label.append(0)
                left.append(s)
            else:
                label.append(1)
                right.append(s)
            cnt[s] += 1
        ans = calc_inv(label)

        pos = {k: [] for k in C.keys()}
        for i, s in enumerate(left):
            pos[s].append(i)
        label = []
        for s in right:
            label.append(pos[s].pop())
        ans += calc_inv(label[::-1])
        return ans

    else:  # 奇数
        if odd != 1:
            return -1
        half = {k: v // 2 for k, v in C.items()}
        cnt = {k: 0 for k in C.keys()}
        label = []
        right = []
        left = []
        seen = 0
        LL = 0  # midの右にあるL
        RR = 0  # midの左にあるR

        for i, s in enumerate(S):
            if s == mid and cnt[s] == half[s]:
                seen = 1
                cnt[s] += 1
                continue
            if cnt[s] < half[s]:
                label.append(0)
                left.append(s)
                if seen:
                    LL += 1
            else:
                label.append(1)
                right.append(s)
                if not seen:
                    RR += 1
            cnt[s] += 1
        ans = calc_inv(label)
        ans += RR + LL

        pos = {k: [] for k in C.keys()}
        for i, s in enumerate(left):
            pos[s].append(i)
        label = []
        for s in right:
            label.append(pos[s].pop())
        ans += calc_inv(label[::-1])
        return ans


print(main())