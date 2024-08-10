def max_sales_volume():
    N = int(input())
    sales = 0
    
    for _ in range(N):
        customers = list(map(int, input().split()))[1:]
        customers.sort(reverse=True)
        
        for i in range(len(customers)):
            sales += min(i+1, customers[i])
    
    print(sales)

max_sales_volume()