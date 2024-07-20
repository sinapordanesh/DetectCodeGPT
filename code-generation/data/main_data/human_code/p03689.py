import sys
def MI(): return map(int,sys.stdin.readline().rstrip().split())


H,W,h,w = MI()
q1,r1 = H//h,H % h
q2,r2 = W//w,W % w

if r1 == 0 and r2 == 0:
    print('No')
else:
    print('Yes')
    if r2 != 0:
        A = []
        for _ in range(q2):
            A += [2*10**6]*(w-1)+[-(2*10**6)*(w-1)-1]
        A += [2*10**6]*r2
        for _ in range(H):
            print(*A)
    else:
        for i in range(1,H+1):
            if i % h != 0:
                print(*([2*10**6]*W))
            else:
                print(*([-(2*10**6)*(h-1)-1]*W))
