import sys


def find_permutation(aaa, use):
    """
    iの残り使用数がaaa[i-1]の状態で
    集合useにある文字群(1～k)を後ろに繋げる方法で
    それよりさらに後が破綻しないような繋げ方のうち
    辞書順最小のものを求める。

    ただし（この関数からは見えないが）現在確定済み配列の
    末尾 (k - |use|) 個は、useに含まれない要素が1回ずつ登場することを前提とする。
    （つまり、この関数の結果を繋げると、末尾 k 個が順列になる）

    どうやっても破綻する場合はNoneを返す。

    :param aaa:
    :param use:
    :return:
    """

    max_a = -1
    min_a = 1005
    max_fixed = -1

    for i in range(k):
        a = aaa[i]
        if i + 1 in use:
            min_a = min(min_a, a)
            max_a = max(max_a, a)
        else:
            max_fixed = max(max_fixed, a)

    if max(max_a, max_fixed + 1) > 2 * min_a:
        return None

    if max_a < 2 * min_a:
        return sorted(use)

    front = []
    rear = []
    either = []
    for i in use:
        if aaa[i - 1] == max_a:
            front.append(i)
        elif aaa[i - 1] == min_a:
            rear.append(i)
        else:
            either.append(i)

    max_front = front[-1]
    for i in either:
        if i < max_front:
            front.append(i)
        else:
            rear.append(i)
    front.sort()
    rear.sort()
    front.extend(rear)

    return front


def solve(k, aaa):
    if k == 1:
        return [1] * aaa[0]

    min_a = min(aaa)
    max_a = max(aaa)
    if min_a * 2 < max_a:
        return [-1]

    ans = []
    ans.extend(find_permutation(aaa, set(range(1, k + 1))))
    for i in range(k):
        aaa[i] -= 1

    remaining = sum(aaa)
    while remaining:
        use = set(range(1, k + 1))
        candidates = []
        for r in range(k):
            result = find_permutation(aaa, use)
            if result is not None:
                candidates.append(result)

            use.remove(ans[-r - 1])
        adopted = min(candidates)
        ans.extend(adopted)
        for i in adopted:
            aaa[i - 1] -= 1
        remaining -= len(adopted)

    return ans


k, *aaa = map(int, sys.stdin.buffer.read().split())
print(*solve(k, aaa))
