from copy import deepcopy

def getval():
    n = int(input())
    return n

def main(n):
    mod = 10**9 + 7
    #A:0 C:1 G:2 T:3
    dp = [[[1 for i in range(4)] for i in range(4)] for i in range(4)]
    dp[0][2][1] = 0
    dp[0][1][2] = 0
    dp[2][0][1] = 0

    def pow4(arr):
        ans = 0
        for i in range(4):
            ans += arr[i]*(4**(3-i))
        return ans 

    p = []
    for i in range(4):
        p.append(pow4([0,2,1,i]))
        p.append(pow4([0,1,2,i]))
        p.append(pow4([2,0,1,i]))
        p.append(pow4([i,0,2,1]))
        p.append(pow4([i,0,1,2]))
        p.append(pow4([i,2,0,1]))
        p.append(pow4([0,i,2,1]))
        p.append(pow4([0,2,i,1]))

    it1 = iter(p)
    it2 = iter(p)
    co = 0
    di = dict(zip(it1,it2))
    for i in range(n-3):
        temp = [[[0 for i in range(4)] for i in range(4)] for i in range(4)]
        for a in range(4):
            for b in range(4):
                for c in range(4):
                    for d in range(4):
                        if pow4([a,b,c,d]) in di:
                            temp[b][c][d] += 0
                        else:
                            temp[b][c][d] += dp[a][b][c]
                            temp[b][c][d] %= mod
        dp = temp

    ans = 0
    if n>=4:
        for i in range(4):
            for j in range(4):
                for k in range(4):
                    ans += temp[i][j][k]
    elif n==3:
        ans = 61
    ans %= mod
    print(ans)

if __name__=="__main__":
    n = getval()
    main(n)