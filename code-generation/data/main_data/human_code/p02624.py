from numba import njit, i8


@njit(i8(i8))
def solve(N):
    ans = 0
    for i in range(1, N + 1):
        j = N // i
        ans += j * (j + 1) // 2 * i
    return ans


N = int(input())
print(solve(N))
