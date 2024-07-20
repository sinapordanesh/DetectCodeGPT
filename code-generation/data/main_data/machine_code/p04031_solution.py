def min_total_cost():
    N = int(input())
    a = list(map(int, input().split()))
    
    avg = sum(a) / N
    total_cost = 0
    
    for i in a:
        total_cost += (i - avg) ** 2
    
    print(total_cost)

min_total_cost()