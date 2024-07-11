def resolve():
    n = int(input())
    if n % 2 == 1:
        print((n//2+1)/n)
    else:
        print(n//2/n)
resolve()