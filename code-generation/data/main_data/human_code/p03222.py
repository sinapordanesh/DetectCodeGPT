from itertools import combinations

def getval():
    h,w,k = map(int,input().split())
    return h,w,k

def main(h,w,goal):
    dp = [0 for i in range(w)]
    dp[0] = 1
    mod = 10**9 + 7
    for i in range(h):
        temp = [0 for i in range(w)]
        for j in range(w):
            for comb in combinations(range(w-1),j):
                arr = [k for k in comb]
                arr.sort()
                flag = False
                for k in range(len(arr)-1):
                    if arr[k]+1==arr[k+1]:
                        flag = True
                        break
                if flag:
                    continue
                for k in range(w):
                    if k in arr:
                        temp[k+1] += dp[k]
                        temp[k+1] %= mod
                    elif k-1 in arr:
                        temp[k-1] += dp[k]
                        temp[k-1] %= mod
                    else:
                        temp[k] += dp[k]
                        temp[k] %= mod
        dp = temp
    print(dp[goal-1]%mod)
                
                
if __name__=="__main__":
    h,w,k= getval()
    main(h,w,k)