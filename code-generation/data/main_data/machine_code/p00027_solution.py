def day_of_week():
    while True:
        m, d = map(int, input().split())
        if m == 0 and d == 0:
            break
        days = ["Thursday", "Friday", "Saturday", "Sunday", "Monday", "Tuesday", "Wednesday"]
        total_days = sum([31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31][:m-1]) + d - 1
        print(days[total_days % 7])

day_of_week()