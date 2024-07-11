n, k = map(int, input().split())

# kのべき乗でnを超える最大の冪数を求める
# 最大の冪数から順にとり尽くしていく
# 再帰で書ける？

def max_beki(number, k):
    beki = 0
    while k**beki <= number:
        beki += 1
    return beki

res = []
waru_kazu = k**(max_beki(n, k) - 1)
while waru_kazu >= 1:
    shou = n//waru_kazu
    res.append(str(shou))
    n -= shou*waru_kazu
    waru_kazu /= k

print(len(res))