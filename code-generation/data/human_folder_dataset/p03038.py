from collections import defaultdict
import sys
input = sys.stdin.readline

def main():
    N, M = map(int, input().split())
    A = list(map(int, input().split()))
    d = defaultdict(int)
    for a in A:
        d[a] += 1
    for _ in range(M):
        B, C = map(int, input().split())
        d[C] += B

    ans = 0
    total_freq = 0
    for v, freq in sorted(d.items(), reverse=True):
        if total_freq + freq <= N:
            ans += v * freq
            total_freq += freq
        else:
            ans += v * (N - total_freq)
            break
    print(ans)


if __name__ == '__main__':
    main()
