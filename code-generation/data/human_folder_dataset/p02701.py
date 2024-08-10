def resolve():
    n = int(input())
    s = [input() for _ in range(n)]
    print(len(set(s)))
resolve()