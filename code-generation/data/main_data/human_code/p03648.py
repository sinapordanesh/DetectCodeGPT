import sys

sys.setrecursionlimit(10 ** 7)
input = sys.stdin.readline
f_inf = float('inf')
mod = 10 ** 9 + 7


def resolve():
    k = int(input())
    nums = list(range(50))

    if k <= 50:
        for i in range(k):
            for j in range(50):
                if j == i:
                    nums[j] += 50
                else:
                    nums[j] -= 1
        print(50)
        print(*nums)
    else:
        q, r = divmod(k, 50)
        nums = [num + q for num in nums]
        for i in range(r):
            for j in range(50):
                if j == i:
                    nums[j] += 50
                else:
                    nums[j] -= 1
        print(50)
        print(*nums)


if __name__ == '__main__':
    resolve()
