import sys

N,K=map(int,input().split())
S=list(input())
MIN=min(S)

def minimum(S):
    T=S+S[::-1]

    ANS=[]

    for i in range(N+1):
        ANS.append(T[i:i+N])

    return min(ANS)

def next(S):
    T=S+S[::-1]
    LIST=[]
    CL=[0]*2*N
    count=0

    for i in range(2*N):
        if T[i]==MIN:
            count+=1

        else:
            count=0

        CL[i]=count

    MAX=max(CL)
    LIST=[]

    for i in range(N-1,2*N):
        if CL[i]==MAX:
            LIST.append(T[i+1-N:i+1])

    return LIST,MAX

def next2(S,x):
    return [MIN]*x+S[x:][::-1]

if K==1:
    print("".join(minimum(S)))

else:
    CAN,MAX=next(S)

    if (MAX<<(K-1))>=N:
        print(MIN*N)
        sys.exit()

    ANS=[]

    for c in CAN:

        ANS.append(next2(c,MAX*((1<<(K-1))-1)))

    print("".join(min(ANS)))