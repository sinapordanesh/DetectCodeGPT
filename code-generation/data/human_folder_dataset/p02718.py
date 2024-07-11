N,M=map(int,input().split())
A=input()
def ans161(N:int, M:int, A:str):
    A=sorted(list(map(int,A.split())))
    if A[-M]< sum(A)/(4*M):
        return "No"
    else:
        return "Yes"
print(ans161(N,M,A))