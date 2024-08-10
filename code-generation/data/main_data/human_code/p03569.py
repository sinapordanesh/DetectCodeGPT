
def resolve():
    S = input()
    l, r = 0, len(S) - 1
    ans = 0
    while l < r:
        # 次に進める
        if S[l] == S[r]:
            l += 1
            r -= 1
        # r位置にxを追加
        elif S[l] == "x":
            ans += 1
            l += 1
        # l位置にxを追加
        elif S[r] == "x":
            ans += 1
            r -= 1
        else:
            print(-1)
            return

    print(ans)


if __name__ == "__main__":
    resolve()