mod = 10**9+7
def mult(A, B):
    C = [[0 for i in range(len(A))] for i in range(len(A))]

    for i in range(len(A)):
        for j in range(len(A)):
            for k in range(len(A)):
                C[i][j] = (C[i][j]+A[i][k]*B[k][j])%mod
    
    return C

def exp(A, p):
    ans = [[0 for i in range(len(A))] for i in range(len(A))]
    for i in range(len(A)):
        ans[i][i] = 1
    
    while p:
        if p%2 == 0:
            A = mult(A, A)
            p = p//2
        else:
            ans = mult(ans, A)
            p -= 1
    
    return ans

n, k = map(int, input().strip().split())
grid = [list(map(int, input().strip().split())) for i in range(n)]

print(sum([sum(i)%mod for i in exp(grid, k)])%mod)



