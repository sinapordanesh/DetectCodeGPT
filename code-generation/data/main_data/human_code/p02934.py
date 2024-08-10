def resolve():
    n = int(input())
    a = [1/(int(i)) for i in input().split()]
    print(1/sum(a))
resolve()