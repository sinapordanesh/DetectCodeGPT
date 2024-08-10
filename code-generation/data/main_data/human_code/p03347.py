def main():
    n = int(input())
    a = []
    for _ in range(n):
        a.append(int(input()))
    x = a[-1]
    ans = a[-1]
    for i in range(1,n):
        if x==0:
            x = a[-1-i]
        e = x-1
        if e>a[-1-i]:
            print(-1)
            return
        elif e<a[-1-i]:
            x = a[-1-i]
            ans += a[-1-i]
        else:
            x -= 1
    if x==0:
        print(ans)
    else:
        print(-1) 

if __name__ == "__main__":
    main()