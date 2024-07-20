def int_list(sepalate=" "): return list(map(int, input().split(sepalate)))


def solve1(n, k, x):
    ans = 0

    for i in range(n):
        ans += min(abs(k-x[i]), x[i]) * 2

    return ans


n = int(input())
k = int(input())
x = int_list()
print(solve1(n, k, x))
