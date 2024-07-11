import sys
import math


# \n
def input():
    return sys.stdin.readline().rstrip()


def main():
    mod = 10 ** 9 + 7

    N,K=map(int,input().split())

    C =[0] *(K+1)

    for k in range(K,1,-1):
        num = K//k
        count = pow(num,N,mod)
        while num>1:
            count -= C[num*k]
            count %=mod
            num-=1
        C[k] =count
    ans =0
    for i in range(K+1):
        ans += i*C[i]
        ans %=mod
    ans += pow(K,N,mod) -sum(C)

    print(ans%mod)



if __name__ == "__main__":
    main()
