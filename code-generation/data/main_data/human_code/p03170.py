def getval():
    n,k = map(int,input().split())
    a = list(map(int,input().split()))
    return n,k,a

def main(n,k,a):
    #Dp such that when the first takes the turn with i remaining stones,
    #0->Second, 1->First wins
    dp = [0 for i in range(k+1)]
    for i in range(1,k+1):
        for j in a:
            if j>i:
                break
            if not dp[i-j]:
                dp[i] = 1
    if dp[k]:
      print("First")
    else:
      print("Second")

if __name__=="__main__":
    n,k,a= getval()
    main(n,k,a)  