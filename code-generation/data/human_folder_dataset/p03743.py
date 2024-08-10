import sys

sys.setrecursionlimit(10 ** 6)
int1 = lambda x: int(x) - 1
p2D = lambda x: print(*x, sep="\n")
def II(): return int(sys.stdin.readline())
def MI(): return map(int, sys.stdin.readline().split())
def LI(): return list(map(int, sys.stdin.readline().split()))
def LLI(rows_number): return [LI() for _ in range(rows_number)]
def SI(): return sys.stdin.readline()[:-1]

def main():
    # YouTubeの通り
    dn, s = MI()
    dd = LI()
    qn = II()
    qq = LI()
    qi = [(q - 1, i) for i, q in enumerate(qq)]
    # pos[i]...dd[i]の移動前の位置
    pos = [s]
    for d in dd:
        pos.append(min(pos[-1], abs(d - pos[-1])))
    # print(pos)
    # bb[i]...dd[i]の移動前にこの距離以上の位置にいればゴールに届かないという境目
    bb = [1] * (dn + 1)
    for i in range(dn - 1, -1, -1):
        d = dd[i]
        if d < bb[i + 1] * 2:
            bb[i] = bb[i + 1] + d
        else:
            bb[i] = bb[i + 1]
    # print(bb)
    #    dd0   dd1   dd2   dd3
    # po0   po1   po2   po3   po4
    # bb0   bb1   bb2   bb3   bb4
    # という前後関係なのでq番目(0-origin)のddに魔法をかけるときは
    # pos[q]>=bb[q+1]であるなら妨害可能(YES)
    ans = [""] * qn
    for q, ai in qi:
        if pos[q] >= bb[q + 1]: ans[ai] = "YES"
        else: ans[ai] = "NO"
    print(*ans, sep="\n")

main()
