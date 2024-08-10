import sys


# \n
def input():
    return sys.stdin.readline().rstrip()

def main():

    N=int(input())
    S=list(input())
    K=int(input())

    d = S[K-1]

    for i in range(N):
        if S[i] !=d:
            S[i] ="*"

    print(*S,sep="")



if __name__ == "__main__":
    main()
