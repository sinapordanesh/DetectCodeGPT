def solve(STR):
    CNT, tmp = 0, list(s)
    while len(set(tmp)) > 1:
        CNT += 1
        for i in range(len(tmp) - 1):
            if STR in tmp[i:i+2]:
                tmp[i] = STR
        tmp.pop()
    return CNT


s = input()

ans = 100
for lttr in set(s):
    ans = min(ans, solve(lttr))
print(ans)
