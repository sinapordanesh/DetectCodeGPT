def get_AC_verdict(N, M):
    if N == M:
        print("Yes")
    else:
        print("No") 

#Get inputs
N, M = map(int, input().split())

#Get AC verdict
get_AC_verdict(N, M)