import sys
def I(): return int(sys.stdin.readline().rstrip())
def LS2(): return list(sys.stdin.readline().rstrip())  #空白なし


N = I()
S = [LS2() for _ in range(N)]

# Aj-Ai == Bj-Bi のとき、
# (Ai,Bi) を選んだときの盤面が'よい' ⇔ (Aj,Bj) を選んだときの盤面が'よい'

ans = 0
for a in range(N):
    X = [S[i] for i in range(a,N)] + [S[i] for i in range(a)]
    for i in range(N-1):
        for j in range(i+1,N):
            if X[i][j] != X[j][i]:
                break
        else:
            continue
        break
    else:
        ans += 1

print(ans*N)
