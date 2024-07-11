N=int(input())
D,X=map(int,input().split())
A=[int(input()) for i in range(N)]

def ans092(N:int, D:int, X:int, A:list):
    ans_int=0
    for i in range(N):
        j_count=0
        while True:
            if 1+A[i]*j_count<=D:
                ans_int+=1
                j_count+=1
                continue
            else:
                break
    return ans_int+X

print(ans092(N,D,X,A))