# Σ(i ^ j = k) ai * bj = ckという形で式が表されるとき
# fwht(a)*fwht(b)=fwht(c)が成り立ち高速化できる
# すごく必死に考えると
# a = [p0 p1 p2 ... p2^N-1]
# b = [x0 x1 x2 ... x2^N-1]
# c = [2^N-1 -1 -1 -1 .... -1]
# とするとうまいことaとcに変数が入らない形になるのでfwht(c)/fwht(a)を計算し
# fwht(b)がわかるのでこれを逆変換すればbが求められる
# なお逆変換は b = fwht(fwht(b)) / 要素数で求められる、なぜかは知らない
# またまたなぜかは知らないがこうして求めた答えは各要素に定数が足されたものになるらしい
# 今回はx0 = 0と分かっているのbを[0 x1-x0 ... x2^N-1-x0]と補正してやればよい

N = int(input())
A = [int(i) for i in input().split()]
MOD = 998244353

NN = 1 << N

def fwht(a) :
    i = 1
    while i < NN :
        j = 0
        while j < NN :
            for k in range(i) :
                x, y = a[j+k], a[i+j+k]
                a[j+k], a[i+j+k] = (x + y) % MOD, (x - y) % MOD
            j += i << 1
        i <<= 1

def inv(x) :
    return pow(x, MOD - 2, MOD)

s = inv(sum(A) % MOD)
for i in range(NN) :
    A[i] = (A[i] * s) % MOD
A[0] = (A[0] - 1) % MOD
fwht(A)

B = [- 1] * (NN)
B[0] = (NN-1) % MOD
fwht(B)

C = [(inv(A[i]) * B[i]) % MOD for i in range(NN)]
fwht(C)

for i in range(NN) :
    C[i] = (C[i] * inv(NN)) % MOD

for i in range(NN) :
    print((C[i] - C[0]) % MOD)