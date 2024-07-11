from collections import deque
rand = False
verbose = False

if rand:
    import random
    N, K = 200000, 10000
    A = random.choices(range(-10**9, 10**9), k=N)
else:
    N, K = list(map(int, input().split()))
    A = list(map(int, input().split()))

MOD = 10**9 + 7

def mul(A):
    ret = 1
    for i in range(len(A)):
        ret = (ret * A[i]) % MOD
#        print (ret)
    return ret

if K==N:
    print(mul(A))
    exit()

POS, NEG = list(), list()
for i in range(len(A)):
    if A[i] < 0:
        NEG.append(A[i])
    else:
        POS.append(A[i])

POS.sort(reverse=True)
NEG.sort()

if len(POS)==0 and K%2==1: # must go negative
    print(mul(NEG[-K:]))
    exit()

POS = deque(POS)
NEG = deque(NEG)

ans = list()
while len(ans)<K:
    if len(NEG) <= 1:
        if verbose: print('no more neg numbers')
        ans.append(POS.popleft()) # no negative numbers to add
    elif len(POS) <= 1:
        if verbose: print('no more pos numbers')
        if K-len(ans)>=2:
            ans.append(NEG.popleft())
            ans.append(NEG.popleft())
        else:
            ans.append(POS.popleft())
    elif POS[0]*POS[1] > NEG[0]*NEG[1] or K-len(ans)==1:
        if verbose: print('pos bigger')
        ans.append(POS.popleft())
    else:
        if verbose: print('neg biger')
        ans.append(NEG.popleft())
        ans.append(NEG.popleft())

print(mul(ans))

