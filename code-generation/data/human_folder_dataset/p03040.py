import sys
from heapq import heapify,heappop,heappush
def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり


ans = 0
left,right = [],[]
heapify(left)
heapify(right)
r = 0

Q = I()
for _ in range(Q):
    q = LI()
    if q[0] == 1:
        a,b = q[1:]
        ans += b
        if r == 0:
            heappush(left,-a)
        elif r == 1:
            x1 = -heappop(left)
            ans += abs(a-x1)
            if x1 < a:
                x1,a = a,x1
            heappush(left,-a)
            heappush(right,x1)
        else:
            x1 = -heappop(left)
            x2 = heappop(right)
            if r % 2 == 0:
                ans += max(0,x1-a,a-x2,0)
                heappush(left,-x1)
                if a <= x2:
                    heappush(left,-a)
                    heappush(right,x2)
                else:
                    heappush(left,-x2)
                    heappush(right,a)
            else:
                ans += abs(x1-a)
                heappush(right,x2)
                if a <= x1:
                    heappush(left,-a)
                    heappush(right,x1)
                else:
                    heappush(left,-x1)
                    heappush(right,a)
        r += 1
    else:
        x = -heappop(left)
        print(x,ans)
        heappush(left,-x)
