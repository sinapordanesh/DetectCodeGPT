def getval():
    n = int(input())
    a = list(map(int,input().split()))
    return n,a

def main(n,a):
    init = sum(a)
    dp = [init,init-2*a[0]-2*a[1]]
    #print(dp)
    for i in range(1,n-1):
        prev1 = dp[0]
        prev2 = dp[1]
        dp[0] = max(prev1,prev2)
        dp[1] = max(prev2+2*a[i]-2*a[i+1],prev1-2*a[i]-2*a[i+1])
        #print(dp)
    print(max(dp))

if __name__=="__main__":
    n,a = getval()
    main(n,a)