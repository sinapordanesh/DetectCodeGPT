def getval():
    n,k = map(int,input().split())
    return n,k 

def main(n,k):
    f = [1]
    for i in range(n):
        f.append(f[i]*(i+1))
    maxpair = f[n-1]//(f[2]*f[n-3])
    if k>maxpair:
        print(-1)
    else:
        pair = maxpair
        ans = []
        for i in range(n-1):
            ans.append([1,i+2])
        for i in range(2,n+1):
            for j in range(i,n+1):
                if pair==k:
                    break
                if i==j:
                    continue
                ans.append([i,j])
                pair -= 1
        print(len(ans))
        for i in ans:
            print(str(i[0]) + " " + str(i[1]))

if __name__=="__main__":
    n,k = getval()
    main(n,k)