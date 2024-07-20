#!/usr/bin/env python3
def main():
    import numpy as np

    N = int(input())
    testimony = np.zeros((N, N), dtype=np.int64)
    for i in range(N):
        A = int(input())
        INF = 10 ** 10
        for _ in range(A):
            x, y = map(int, input().split())
            testimony[i, x - 1] += 1 if y else -INF

    # 正直者のパターンをbit全探索
    ans = 0
    for bit in range(1 << N):
        honest = set()
        pick = np.zeros(N, dtype=np.int64)
        for i in range(N):
            if bit & (1 << i):
                honest.add(i)
                pick += testimony[i, :]
        flag = True
        for j in range(N):
            value = pick[j]
            # 下記3つの内1つでも満たしたら，仮定が間違っていると分かる.
            if (0
                    or (j in honest and value < 0)         # 正直者なのに嘘つきと言われる
                    or (j not in honest and value > 0)     # 嘘つきなのに正直者と言われる
                    or (value < 0 and value % INF != 0)):  # 正直とも嘘つきとも言われる
                flag = False
                break
        if flag:
            ans = max(ans, len(honest))
    print(ans)


if __name__ == '__main__':
    main()
