def searchII():
    n = int(input())
    S = set(map(int, input().split()))
    q = int(input())
    T = list(map(int, input().split()))
    
    count = 0
    for num in T:
        if num in S:
            count += 1
    
    print(count)

searchII()