def unique_elements():
    n = int(input())
    arr = list(map(int, input().split()))
    
    result = []
    for i in range(n):
        if i == 0 or arr[i] != arr[i-1]:
            result.append(arr[i])
    
    print(*result)