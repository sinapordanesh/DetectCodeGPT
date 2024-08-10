import sys,queue,math,copy,itertools,bisect,collections,heapq

def main():
    LI = lambda : [int(x) for x in sys.stdin.readline().split()]


    H,W,N = LI()

    d = collections.Counter()
    for _ in range(N):
        x,y = LI()
        for dx in range(-1,2):
            for dy in range(-1,2):
                nx = x+dx
                ny = y+dy
                if 1 < nx < H and 1 < ny < W:
                    d[(nx,ny)] += 1
    ans = [0] * 10
    for x,c in collections.Counter(d.values()).items():
        ans[x] += c
    ans[0] = (H-2) * (W-2) - sum(ans[1:])

    print(*ans,sep='\n')

if __name__ == '__main__':
    main()