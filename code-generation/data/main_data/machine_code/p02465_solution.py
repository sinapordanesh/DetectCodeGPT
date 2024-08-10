def set_difference():
    n = int(input())
    set_A = set(map(int, input().split()))
    m = int(input())
    set_B = set(map(int, input().split()))
    
    result = sorted(list(set_A - set_B))
    for num in result:
        print(num)

set_difference()