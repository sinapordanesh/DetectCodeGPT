import bisect,collections,copy,itertools,math,string
import sys
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))
def S(): return sys.stdin.readline().rstrip()
def LS(): return list(sys.stdin.readline().rstrip().split())
def main():

    h, w, k = LI()
    cake = []
    for _ in range(h):
        row = S()
        row = row.replace(".", "0").replace("#", "1")
        row = list(map(int, row))
        cake.append(row)

    s = [0]
    g = []
    rsum = [sum(cake[i]) for i in range(h)]
    for i in range(h):
        if rsum[i] != 0:
            rsum[i] = 0
            break
    for i in range(h):
        if rsum[i] != 0:
            s.append(i)
            g.append(i)
    g.append(h)

    cnt = 0
    ans = []

    for i in range(len(s)):
        row_t = list(zip(*cake[s[i]:g[i]]))
        tsum = [sum(row_t[j]) for j in range(len(row_t))]
        for j in range(len(row_t)):
            if tsum[j] != 0:
                tsum[j] = 0
                break
        cnt += 1
        for j in range(len(row_t)):
            if tsum[j] == 1:
                cnt += 1
            row_t[j] = [cnt for _ in range(len(row_t[j]))]
        row = list(zip(*row_t))
        ans += row

    for row in ans:
        print(*row)


main()



