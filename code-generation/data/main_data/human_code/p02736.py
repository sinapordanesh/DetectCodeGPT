def solve_for_01(nums):
    # nums: 各要素が 0 or 1 のリスト。
    # 「x_{i+1, j} = x_{i, j} ^ x_{i, j+1} で定義。x_{N, 1} は？」という問題を解く。
    # a_{i} は (N-1)_C_i 回作用するので、(N-1)_C_i の偶奇で a_{i} が残るか否かが決まる。
    # (N-1)_C_i の偶奇については Lucasの定理から
    #   (N-1) & i == i <=> 奇数
    #   (N-1) & i != i <=> 偶数
    # が言える。
    N = len(nums)
    ans = 0
    for i, x in enumerate(nums):
        if (N - 1) & i == i:
            ans ^= x
    return ans


def main():
    # ref: https://atcoder.jp/contests/agc043/submissions/16398495
    N = int(input())
    A = list(map(lambda x: int(x) - 1, input()))
    if 1 in A:
        # 1が含まれる場合は答えは0 or 1になる。
        # 答えの偶奇だけ合致してればよいので、2 -> 0で置き換えて問題を解いてもこのケースでは大丈夫。
        print(solve_for_01([a % 2 for a in A]))
    else:
        # 1が含まれない場合はすべての数字は0 or 2。
        # 2で割ることで、すべての数字が0 or 1のケースに帰着可能。
        print(solve_for_01([a // 2 for a in A]) * 2)


if __name__ == '__main__':
    main()