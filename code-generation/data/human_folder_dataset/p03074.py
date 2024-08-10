
from itertools import accumulate
def resolve():
    N, K = map(int, input().split())
    S = input()

    # even:1
    # odd:0
    # 1-0-1-0-1 の配列にする. 両端は1にする
    L = []
    pre = "1"
    cnt = 0
    for i in range(N):
        if pre == S[i]:
            cnt += 1
        else:
            L.append(cnt)
            cnt = 1
        pre = S[i]
    L.append(cnt)
    # 最後が0で終わっていたら、仮の1を付け足す。(値が0なので影響ない)
    if pre == "0":
        L.append(0)

    # 1-0-1-0-1の配列を作成し、K＝2だとする。
    # 0を2個含めた個数は, 1＝3、0＝2の長さが作成できる
    length = 2 * K + 1

    # 0をすべて変換できる
    if len(L) <= length:
        return print(N)

    # 1-0-1-0-1の配列なので間に0を含んだ数え上げ
    # なので偶数とびに1を起点に数え上げ
    # 累積
    acc = [0] + list(accumulate(L))
    ans = 0
    for i in range(0, len(L), 2):
        left = i
        right = min(i + length, len(L))
        tmp = acc[right] - acc[left]

        ans = max(ans, tmp)

    print(ans)


if __name__ == "__main__":
    resolve()
