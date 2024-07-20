def out(n):
    mask = 2**32 -1
    print(format(n&mask,"032b"))

n = int(input())

out(n)
out(~n)
out(n<<1)
out(n>>1)

