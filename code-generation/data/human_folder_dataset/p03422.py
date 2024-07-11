import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

n = int(readline())
data = list(map(int,read().split()))

def calc_g(x,k):
    while(x>=k):
        if(x%k==0):
            return x//k
        fn = x//k
        x1 = x - (fn + 1)
        x2 = fn*k + (x%k)%(fn+1)
        x = min(x1,x2)
    return 0

grundy = 0
it = iter(data)
for a,k in zip(it,it):
    grundy = grundy ^ calc_g(a,k)

if(grundy==0):
    print('Aoki')
else:
    print('Takahashi')