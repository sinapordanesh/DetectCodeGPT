import sys

def I(): return int(sys.stdin.readline().rstrip())
def LI(): return list(map(int,sys.stdin.readline().rstrip().split()))  #空白あり

N = I()
A = LI()

if N == 1:
    print('Second')
    exit()

if N == 2:
    print('First')
    exit()

from math import gcd

r = 0  # 0:高橋君の番、1:青木君の番
while True:
    if (sum(A)-N) % 2 == 1:
        if r == 0:
            print('First')
        else:
            print('Second')
        break
    else:
        a = 0  # 奇数の要素の個数
        b = 0  # 1の個数
        for i in range(N):
            if A[i] % 2 == 1:
                a += 1
            if A[i] == 1:
                b += 1
        if a != 1 or b > 0:
            if r == 0:
                print('Second')
            else:
                print('First')
            break
        else:
            g = 0
            for i in range(N):
                if A[i] % 2 == 1:
                    g = gcd(g,A[i]-1)
                else:
                    g = gcd(g,A[i])
            for i in range(N):
                A[i] = A[i]//g
            r = 1-r
