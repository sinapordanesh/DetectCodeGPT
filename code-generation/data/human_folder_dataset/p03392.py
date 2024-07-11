def main():
    md = 998244353
    s = input()
    n = len(s)
    al = True  # allすべて同じ文字
    an = 1  # any連続が存在すると0
    for c0, c1 in zip(s, s[1:]):
        if c0 == c1:
            an = 0
        else:
            al = False
        if an == 0 and not al: break
    if al:
        print(1)
        exit()
    if n == 2:
        print(2)
        exit()
    if n == 3:
        if s[0] == s[-1]:
            print(7)
        elif s[0] == s[1] or s[1] == s[2]:
            print(6)
        else:
            print(3)
        exit()
    #print(n)
    #print(an)
    ord0=ord("a")
    r = sum(ord(c) - ord0 for c in s) % 3
    if n%3==0:
        d=pow(2,n//3-1,md)
        if r==0:
            an-=d*2
        else:
            an+=d
    print((pow(3, n - 1, md) - pow(2, n - 1, md) + an) % md)

main()
