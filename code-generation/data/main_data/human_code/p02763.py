from typing import List, Any


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


class SegmentTree:
    
    def __init__(self, array):
        self.n = len(array)
        self.array = [0 for _ in array]+array
        for i in range(self.n-1, 0, -1):
            self.array[i] = self.array[i<<1]|self.array[i<<1|1]

    def set(self, i, v):
        p = self.n+i
        self.array[p] = v
        while p > 1:
            p >>= 1
            self.array[p] = self.array[p<<1]|self.array[p<<1|1]

    def count(self, l, r):
        l += self.n
        r += self.n
        answer = 0
        while l < r:
            if l&1:
                answer |= self.array[l]
                l += 1
            if r&1:
                r -= 1
                answer |= self.array[r]
            l >>= 1
            r >>= 1
        return answer


def bit_count(a):
    answer = 0
    while a:
        answer += a&1
        a >>= 1
    return answer


def solve():
    ALPHABETS = 'abcdefghijklmnopqrstuvwxyz'
    N = read_int()
    S = input()
    Q = read_int()
    segment_tree = SegmentTree([1<<(ALPHABETS.index(c)) for c in S])
    for _ in range(Q):
        cmd = input().strip().split(' ')
        if cmd[0] == '1':
            n = 1<<(ALPHABETS.index(cmd[2]))
            segment_tree.set(int(cmd[1])-1, n)
        else:
            l, r = int(cmd[1])-1, int(cmd[2])
            print(bit_count(segment_tree.count(l, r)))


if __name__ == '__main__':
    solve()
