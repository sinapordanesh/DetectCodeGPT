import sys
read = sys.stdin.buffer.read
readline = sys.stdin.buffer.readline
readlines = sys.stdin.buffer.readlines

import numpy as np

MOD = 998244353

N,M = map(int,readline().split())
A,B,C,D = [np.array(list(readline().rstrip()))-48 for _ in range(4)]

def cumprod(arr,MOD):
    L = len(arr); Lsq = int(L**.5+1)
    arr = np.resize(arr,Lsq**2).reshape(Lsq,Lsq)
    for n in range(1,Lsq):
        arr[:,n] *= arr[:,n-1]; arr[:,n] %= MOD
    for n in range(1,Lsq):
        arr[n] *= arr[n-1,-1]; arr[n] %= MOD
    return arr.ravel()[:L]

def make_fact(U,MOD):
    x = np.arange(U,dtype=np.int64); x[0] = 1
    fact = cumprod(x,MOD)
    x = np.arange(U,0,-1,dtype=np.int64); x[0] = pow(int(fact[-1]),MOD-2,MOD)
    fact_inv = cumprod(x,MOD)[::-1]
    return fact,fact_inv

U = 10**6
fact, fact_inv = make_fact(U,MOD)

def cnt_vertical(N,M,A,B,C,D):
    """
    ・ABが長さN、CDが長さM。
    ・初手に縦線を入れる場合。
    ・縦線の右端の位置に応じて場合分けして集計
    ・右端の位置を決めると、（左端の位置ごとの左側の入れ方の累積和） x （右側の入れ方の累積和）、適当に重みをつける必要あり
    """
    AB=A+B
    # ある場所を初めての縦線としたときに、左側にできる部分。上にある点の個数と下にある点の個数
    L=C.sum(); LU=A.cumsum()-A; LD=B.cumsum()-B
    NL=fact[LU+LD+L-1]*fact_inv[LU+LD]%MOD*fact_inv[L-1]% MOD

    R=D.sum(); RU=A[::-1].cumsum()-A[::-1]; RD=B[::-1].cumsum()-B[::-1]
    NR=fact[RU+RD+R-1]*fact_inv[RU+RD]%MOD*fact_inv[R-1]%MOD; NR=NR[::-1]

    x=np.ones(N,np.int64); x[AB==2]=2; coef=cumprod(x,MOD)
    x=np.ones(N,np.int64); x[AB==2]=(MOD+1)//2; coef_inv=cumprod(x,MOD)
    NL*=coef_inv; NR*=coef; NL%=MOD; NR%=MOD
    NL[AB==2]*=2
    NL[AB==0]=0;NR[AB==0]=0
    NL_cum=NL.cumsum()%MOD
    return (NL_cum*NR%MOD).sum()%MOD

def AB_only(N,A,B):
    x = np.ones(N,np.int64)
    x[A+B==2] = 2
    return cumprod(x,MOD)[-1]

def ABC_only(N,M,A,B,C):
    AB=A+B
    NA,NB,NC = [np.count_nonzero(x) for x in [A,B,C]]
    R=NC;RU=A[::-1].cumsum()-A[::-1];RD=B[::-1].cumsum()-B[::-1]
    NR=fact[RU+RD+R-1]*fact_inv[RU+RD]%MOD*fact_inv[R-1]%MOD; NR=NR[::-1]
    NR[AB==0]=0
    x=np.ones(N,np.int64); x[AB==2]=2; coef=cumprod(x,MOD)
    x=(coef*NR% MOD).sum()%MOD
    y=fact[NA+NB+NC-1]*fact_inv[NC-1]%MOD*fact_inv[NA+NB]%MOD
    return (x+y)%MOD

def F(N,M,A,B,C,D):
    # 問題の答えを出します。
    NA,NB,NC,ND = [np.count_nonzero(x) for x in [A,B,C,D]]
    if all(x != 0 for x in [NA,NB,NC,ND]):
        return (cnt_vertical(N,M,A,B,C,D) + cnt_vertical(M,N,C,D,A,B)) % MOD
    # A,Cに0列を寄せる
    if NA != 0:
        NA,NB = NB,NA; A,B = B,A; C = C[::-1]; D = D[::-1]
    if NC != 0:
        NC,ND = ND,NC; C,D = D,C; A = A[::-1]; B = B[::-1]
    if NB == 0:
        return AB_only(M,C,D)
    if ND == 0:
        return AB_only(N,A,B)
    # B,Dは0ではない
    if NA == 0 and NC == 0:
        # 2面B,Dのみ -> binom(B+D,B)
        return fact[NB+ND] * fact_inv[NB] % MOD * fact_inv[ND] % MOD
    if NA == 0:
        return ABC_only(M,N,C,D,B)
    if NC == 0:
        return ABC_only(N,M,A,B,D)

answer = F(N,M,A,B,C,D)
print(answer)