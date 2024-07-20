LOG = 18

def main():
    S = input()
    N = len(S)
    to = []
    for _ in range(LOG):
        l = [0]*N
        to.append(l)
        
    for i in range(N):
        to[0][i] = i + 1 if S[i] == "R" else i -1
    
    for i in range(1, LOG):
        for j in range(N):
            to[i][j] = to[i-1][to[i-1][j]]
            
    ans = [0]*N
    for j in range(N):
        ans[to[LOG-1][j]] += 1
        
    print(*ans)
    return

main()