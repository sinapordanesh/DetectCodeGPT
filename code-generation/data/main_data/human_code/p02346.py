
class SegmentTree:
    def __init__(self, n):
        size = 1
        while size < n:
            size *= 2
        self.size = 2*size - 1
        self.data = [0] * self.size

    def add(self, i, v):
        # assert 0 <= i <= self.size//2
        index = self.size // 2 + i
        self.data[index] += v
        while index > 0:
            index = (index-1) // 2
            self.data[index] = self.data[index*2 + 1] + self.data[index*2 + 2]

    def sum(self, lo, hi):
        def _sum(r, i, j):
            if j < lo or i > hi:
                return 0
            elif lo <= i and j <= hi:
                return self.data[r]
            else:
                mid = i + (j - i)//2
                return _sum(r*2 + 1, i, mid) + _sum(r*2 + 2, mid+1, j)

        # assert 0 <= lo <= self.size//2
        # assert 0 <= hi <= self.size//2
        # assert lo <= hi

        return _sum(0, 0, self.size//2)


def run():
    n, q = [int(i) for i in input().split()]

    t = SegmentTree(n)
    for _ in range(q):
        com, x, y = [int(i) for i in input().split()]
        if com == 0:
            t.add(x-1, y)
        else:
            print(t.sum(x-1, y-1))


if __name__ == '__main__':
    run()

