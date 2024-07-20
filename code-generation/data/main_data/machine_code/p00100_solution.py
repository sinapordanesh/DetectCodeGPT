def identify_good_workers():
    while True:
        n = int(input())
        if n == 0:
            break
        total_sales = {}
        for _ in range(n):
            employee_id, price, quantity = map(int, input().split())
            total_sales[employee_id] = total_sales.get(employee_id, 0) + price * quantity
        result = [key for key, value in total_sales.items() if value >= 1000000]
        if result:
            for i in result:
                print(i)
        else:
            print("NA")

identify_good_workers()