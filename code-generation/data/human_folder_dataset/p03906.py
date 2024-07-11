import sys
import numpy as np
import numba
from numba import njit
i8 = numba.int64

read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

@njit((i8[:], i8), cache=True)
def solve(A, keta):
    # 10^keta の位を n にできるか
    MOD = 10**(keta + 1)
    B = 10**keta
    nums = [0]
    for x in A:
        x %= MOD
        n = len(nums)
        for i in range(n):
            s = nums[i] + x
            if s >= MOD:
                s -= MOD
            nums.append(s)
        nums.sort()
        # x, y, z とあって、x + z < B ならば、y は捨ててよい
        tmp = []
        for x in nums:
            while len(tmp) >= 2 and tmp[-2] + B > x:
                tmp.pop()
            tmp.append(x)
        nums = tmp
    return nums[-1] // B

def main(A):
    N = len(A)
    ans = 0
    for keta in range(18):
        x = solve(A, keta)
        ans += x
    return ans

A = np.array(read().split(), np.int64)[1:]
np.random.shuffle(A)
print(main(A))