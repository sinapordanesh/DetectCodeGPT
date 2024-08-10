def minimum_total_cost():
    N = int(input())
    a = list(map(int, input().split()))
    
    total_cost = 0
    target = sum(a) / N
    
    for num in a:
        total_cost += (num - target) ** 2
        
    print(total_cost)

minimum_total_cost()