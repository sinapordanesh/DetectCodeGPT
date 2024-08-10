import sys
X,Y = map(int,input().split())
if (X+Y)%3 != 0:
    print(0)
    sys.exit()
A = Y - (X+Y)//3
B = X - (X+Y)//3
if A<0 or B<0:
    print(0)
    sys.exit()
N = A+B
def cmb(n, r, mod):
    inv = [0,1]
    for i in range(2, N + 1):
        inv.append((-inv[mod % i] * (mod // i)) % mod)
    cmd = 1
    for i in range(1,min(r,n-r)+1):
        cmd = (cmd*(N-i+1)*inv[i])%mod
    return cmd
    
a = cmb(N,A,10**9+7)
print(a)