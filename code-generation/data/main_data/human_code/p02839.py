def getval():
    h,w = map(int,input().split())
    a = [list(map(int,input().split())) for i in range(h)]
    b = [list(map(int,input().split())) for i in range(h)]
    return h,w,a,b

def main(h,w,a,b):
    dp = []
    for i in range(w):
        dp.append([False for j in range(1+160*(i+1))])

    dp[0][abs(a[0][0]-b[0][0])] = True
    for i in range(w-1):
        cura = a[0][i+1]
        curb = b[0][i+1]
        prev = dp[i]
        for j in range(len(prev)):
            if prev[j]:
                u1 = abs(j-(cura-curb))
                u2 = abs(j-(curb-cura))
                for k in [u1,u2]:
                    if k<=160*80:
                        dp[i+1][k] = True
    #for i in dp:
      #print(i[:20])
    for i in range(h-1):
        temp = []
        rowa = a[i+1]
        rowb = b[i+1]
        for j in range(w):
            cur = [False for k in range(min(1+160*(i+j+2),1+160*80))]
            prev1 = dp[j]
            prev2 = dp[j]
            if temp:
                prev2 = temp[-1]
            cura = rowa[j]
            curb = rowb[j]
            for k in range(len(prev1)):
                if prev1[k] or prev2[k]:
                    u1 = abs(k-(cura-curb))
                    u2 = abs(k-(curb-cura))
                    if u1<len(cur):
                        cur[u1] = True
                    if u2<len(cur):
                        cur[u2] = True
            temp.append(cur)
        dp = temp
        #for i in dp:
          #print(i[:20])

    ans = 0
    for i in range(160*80+1):
        if dp[-1][i]:
            ans = i 
            break
    print(ans)        

if __name__=="__main__":
    h,w,a,b = getval()
    main(h,w,a,b)