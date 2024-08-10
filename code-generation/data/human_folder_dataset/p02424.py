def out(n):
    mask = 2**32 -1
    print(format(n&mask,"032b"))


a,b = map(int,input().split())
out(a&b)
out(a|b)
out(a^b)

