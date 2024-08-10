
def resolve():
    N = int(input())
    S = input()

    # '#.'という箇所が1箇所でもあるとダメなので、ある場所に黒が現れたら
    # 、そこから右は全て黒にならないといけない

    Wt = [0] * (N + 1)
    Bl = [0] * (N + 1)

    for i in range(N):
        if S[i] == "#":
            Bl[i + 1] = Bl[i] + 1
            Wt[i + 1] = Wt[i]
        else:
            Wt[i + 1] = Wt[i] + 1
            Bl[i + 1] = Bl[i]

    ans = 1 << 60
    for i in range(N + 1):
        tmp = 0
        # left を全部白に
        tmp += Bl[i] - Bl[0]

        # right を全部黒に
        tmp += Wt[N] - Wt[i]

        ans = min(ans, tmp)

    print(ans)


if __name__ == "__main__":
    resolve()