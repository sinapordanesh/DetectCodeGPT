def weather_forecast(period):
    def has_rain(day):
        for field in day:
            if field in [6, 7, 10, 11]:
                return True
        return False

    def check_schedule(schedule):
        cloud_positions = [(0, 0), (0, 1), (1, 0), (1, 1)]
        for day in schedule:
            if has_rain(day):
                cloud_positions = [(i+1, j+1) for i, j in cloud_positions]
            else:
                for i, row in enumerate(day):
                    for j, field in enumerate(row):
                        if field == 1 and (i+1, j+1) not in cloud_positions:
                            return 0
        return 1

    for _ in range(period):
        N = int(input())
        if N == 0:
            break
        schedule = [list(map(int, input().split())) for _ in range(N)]
        print(check_schedule(schedule))

# Test the function with the sample input
weather_forecast(3)