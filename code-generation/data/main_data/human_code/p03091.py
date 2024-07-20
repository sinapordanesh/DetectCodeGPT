def main():
    import sys
    input = sys.stdin.readline
    #n = int(input())
    #l = list(map(int, input().split()))
    '''
    a=[]
    b=[]
    for i in range():
        A, B = map(int, input().split())
        a.append(A)
        b.append(B)'''

    n,m=map(int, input().split())
    l=[[]for _ in range(n)]
    cnt=0

    for i in range(m):
        A,B = map(int, input().split())
        l[A-1].append(B-1)
        l[B-1].append(A-1)

    v=[]
    for i in range(n):
        le=len(l[i])
        if le%2!=0:#euler
            print("No")
            return
        if le>=4:
            v.append(i)
    #e>6>4
    for item in v:
        if len(l[item])>=6:
            print("Yes")
            return
    ll=len(v)
    if ll<2:#4*1~0
        print("No")
        return
    elif ll>2:
        print("Yes")
        return

    s,e=v #4*2
    for item in l[s]:
        p=s
        n=item

        while n!=e:
            for jtem in l[n]:
                if jtem!=p:
                    p,n=n,jtem
                    break
            
            if n==s:
                print("Yes")
                sys.exit()

    print("No")

if __name__ == "__main__":
    main()