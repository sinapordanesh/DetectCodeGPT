from copy import deepcopy

def getval():
    n,ma,mb = map(int,input().split())
    p = [list(map(int,input().split())) for i in range(n)]
    return n,ma,mb,p 

def main(n,ma,mb,p):
    dp = [[[-1 for i in range(401)] for i in range(401)]]
    dp[0][0][0] = 0
    for i in range(n):
        temp = deepcopy(dp[-1])
        temp[0][0] = 0
        cur = p[i]
        prev = dp[-1]
        for a in range(401):
            for b in range(401):
                if cur[0]>a or cur[1]>b:
                    continue
                if prev[a-cur[0]][b-cur[1]]==-1:
                    continue
                elif prev[a][b]==-1:
                    temp[a][b] = prev[a-cur[0]][b-cur[1]] + cur[2]
                    #print(i,a,b,temp[a][b],prev[a-cur[0]][b-cur[1]])
                else:
                    temp[a][b] = min(prev[a][b], prev[a-cur[0]][b-cur[1]] + cur[2])
        dp.append(temp)
    ans = -1
    for i in range(1,401):
        if i*ma>400 or i*mb>400:
            break
        if dp[n][i*ma][i*mb]!=-1:
            if ans==-1:
                ans = dp[n][i*ma][i*mb]
            else:
                ans = min(ans,dp[n][i*ma][i*mb])
    print(ans)
    #print(dp[n])

if __name__=="__main__":
    n,ma,mb,p = getval()
    main(n,ma,mb,p)
