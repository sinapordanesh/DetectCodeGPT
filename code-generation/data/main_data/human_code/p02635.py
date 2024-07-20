import numpy as np


def solve(slots_array, K):
    MOD = 998244353
    dp = np.zeros((K+1, K+1), np.int64)
    dp[0][0] = 1
    for i in range(len(slots_array) - 1, -1, -1):
        new_dp = dp.copy()
        for j in range(K, -1, -1):
            for k in range(K-1, -1, -1):
                new_dp[j][k] += new_dp[j][k+1]
        new_dp %= MOD
        for t in range(1, slots_array[i] + 1):
            new_dp[t:, t:] += dp[:-t, :-t]
        dp = new_dp
    # print(dp)
    return np.sum(dp[:K+1, 0]) % MOD

def main():     
    S, K_str = input().split()
    K = int(K_str)

    slots = []
    index = 0
    while index < len(S):
        prev_index = index
        while index < len(S) and S[index] == '1':
            index += 1
        slots.append(index - prev_index)
        index += 1

    K = min(sum(slots) + 1, K)
    print(solve(np.array(slots, np.int64), K))


def cc_export():
    from numba.pycc import CC
    cc = CC('my_module')
    cc.export('solve', 'i8(i8[:], i8)')(solve)
    cc.compile()

if __name__ == '__main__':
    main()