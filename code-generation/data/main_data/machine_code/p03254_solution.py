def distribute_sweets():
    N, x = map(int, input().split())
    a = list(map(int, input().split()))
    a.sort()
    
    count = 0
    for i in range(N):
        if x >= a[i]:
            x -= a[i]
            count += 1
        else:
            break
    
    print(count)

distribute_sweets()