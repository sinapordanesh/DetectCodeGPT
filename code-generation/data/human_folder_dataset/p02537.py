from typing import List, Any
import math
import sys
input = sys.stdin.readline

class SegmentTree:
    
    def __init__(self, array):
        self.n = len(array)
        self.array = [0 for _ in array]+array
        for i in range(self.n-1, 0, -1):
            self.array[i] = max(self.array[i<<1], self.array[i<<1|1])

    def set(self, i, v):
        p = self.n+i
        self.array[p] = v
        while p > 1:
            p >>= 1
            self.array[p] = max(self.array[p<<1], self.array[p<<1|1])

    def max(self, l, r):
        l += self.n
        r += self.n
        answer = 0
        while l < r:
            if l&1:
                answer = max(answer, self.array[l])
                l += 1
            if r&1:
                r -= 1
                answer = max(answer, self.array[r])
            l >>= 1
            r >>= 1
        return answer


def read_int() -> int:
    return int(input().strip())


def read_ints() -> List[int]:
    return list(map(int, input().strip().split(' ')))


def solve() -> Any:
    N, K = read_ints()
    A = [read_int() for _ in range(N)]
    maxA = max(A)
    segment_tree = SegmentTree([0]*(maxA+1))
    for a in A:
        count = segment_tree.max(max(0, a-K), min(maxA, a+K)+1)
        segment_tree.set(a, count+1)
    return segment_tree.max(0, maxA+1)


if __name__ == '__main__':
    print(solve())
