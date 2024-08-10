def resolve():
    n = int(input())
    a = tuple(map(int,input().split()))
    print('YES' if len(a)==len(set(a)) else 'NO')
resolve()