def income_inequality():
    while True:
        n = int(input())
        if n == 0:
            break
        incomes = list(map(int, input().split()))
        average = sum(incomes) / n
        count = 0
        for income in incomes:
            if income <= average:
                count += 1
        print(count)

income_inequality()