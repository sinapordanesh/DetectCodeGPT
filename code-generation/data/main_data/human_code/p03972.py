import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]
    NI = lambda : int(sys.stdin.readline())

    W,H = LI()
    s = []
    for _ in range(W):
        s.append((NI(),0))
    for _ in range(H):
        s.append((NI(),1))
    s.sort()
    x = 0
    y = 0
    ans = 0
    for r,d in s:
        if d == 0:
            ans += (H - y + 1) * r
            x += 1
        else:
            ans += (W - x + 1) * r
            y += 1
    print(ans)

if __name__ == '__main__':
    main()