def best_meeting_date():
    while True:
        N, Q = map(int, input().split())
        if N == 0 and Q == 0:
            break
        dates = {}
        for _ in range(N):
            dates_list = list(map(int, input().split()))[1:]
            for date in dates_list:
                if date not in dates:
                    dates[date] = 1
                else:
                    dates[date] += 1
        max_date = max(dates, key=dates.get) if max(dates.values()) >= Q else 0
        print(max_date)

best_meeting_date()