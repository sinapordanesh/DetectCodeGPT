from itertools import groupby, accumulate


def solve(t):
    grp = [(c, len(list(itr))) for c, itr in groupby(t)]
    even_ones = 0
    zeros_splitting_odd_ones = [0]
    for c, cnt in grp:
        if c == '1':
            if cnt % 2 == 0:
                even_ones += cnt
            else:
                even_ones += cnt - 1
                zeros_splitting_odd_ones.append(0)
        else:
            zeros_splitting_odd_ones[-1] += cnt

    # 初期状態で加算されるか
    ad = int(zeros_splitting_odd_ones[0] % 2 == 0)
    is_added_init = [ad]
    for cnt in zeros_splitting_odd_ones[1:]:
        ad ^= (cnt % 2) ^ 1
        is_added_init.append(ad)
    is_added_init.pop()
    acc_added_init = list(accumulate(reversed(is_added_init)))  # 自分より右で、初期状態で足される1の数
    acc_added_init.reverse()

    odd_ones = len(is_added_init)
    ans = 0

    if odd_ones > 0:

        # 先頭の0を全て除くまでのスコア
        zso = zeros_splitting_odd_ones[0]
        zso1 = zso // 2
        zso0 = zso - zso1
        ans += acc_added_init[0] * zso0
        ans += (odd_ones - acc_added_init[0]) * zso1

        # 1に挟まれた0を1箇所1つずつ残して全て除くまでのスコア
        ad = int(zeros_splitting_odd_ones[0] % 2 == 0)
        for i in range(1, odd_ones):
            zso = zeros_splitting_odd_ones[i] - 1
            zso1 = zso // 2
            zso0 = zso - zso1
            left_ones = i
            right_ones = odd_ones - left_ones
            ans += left_ones * zso  # 区間より左の"1"は全てスコアに足される
            ans += left_ones + (right_ones + 1) // 2  # 最後に1つ残った0を削除するときのスコア
            if ad:
                # 除外中の0区間の次の"1"が初期状態で足されるなら、区間を操作する直前にも足される
                ans += acc_added_init[i] * zso0
                ans += (right_ones - acc_added_init[i]) * zso1
            else:
                # 除外中の0区間の次の"1"が初期状態で足されるなら、区間を操作する直前には足されない
                ans += (right_ones - acc_added_init[i]) * zso0
                ans += acc_added_init[i] * zso1
            ad ^= zso % 2

        # 末尾の0を全て除くまでのスコア
        ans += zeros_splitting_odd_ones[-1] * odd_ones

    # 1だけの列を1つずつ除いていくスコア
    all_ones = odd_ones + even_ones
    ao1 = all_ones // 2
    ao0 = all_ones - ao1
    ans += (ao0 * (ao0 + 1) + ao1 * (ao1 + 1)) // 2

    # 0を除いている間の、偶数個の1によるスコア
    all_zeros = len(t) - all_ones
    ans += all_zeros * (even_ones // 2)

    return ans


t = input()
print(solve(t))
