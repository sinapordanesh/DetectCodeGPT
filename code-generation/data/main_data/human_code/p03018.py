
def resolve():
    S = input()

    rep_S = S.replace("BC", "D")
    cnt = 0
    ans = 0
    for i in range(len(rep_S)):
        if rep_S[i] == "A":
            cnt += 1
        elif rep_S[i] == "D":
            ans += cnt
        else:
            cnt = 0

    print(ans)


if __name__ == "__main__":
    resolve()