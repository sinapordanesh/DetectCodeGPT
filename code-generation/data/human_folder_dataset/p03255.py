# 解説AC
from itertools import accumulate

def main():
    N,X = map(int, input().split())
    T = [0] + [int(i) for i in input().split()]
    S = list(accumulate(T))

    ans = float("inf")
    for k in range(1, N + 1):
        cost = (N + k) * X
        for i, now in enumerate(range(N, 0, -k), start = 1):
            x = S[now] - S[max(0, now - k)]
            cost += 5 * x if (i == 1) else (2 * i + 1) * x

        ans = min(ans, cost)

    print(ans)

if __name__ == "__main__":
    main()