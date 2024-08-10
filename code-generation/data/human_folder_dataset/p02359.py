def main():
    n,t = map(int,input().split())
    t+=1
    T = [0]*t
    for _ in range(n):
        l,r = map(int,input().split())
        T[l]+=1
        T[r]-=1
    num = 0
    res = 0
    for i in range(t):
        num += T[i]
        res = max(num,res)
    print (res)

if __name__ == '__main__':
    main()


