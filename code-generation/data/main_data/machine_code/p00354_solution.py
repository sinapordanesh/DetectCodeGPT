def day_of_week(X):
    days = ["mon", "tue", "wed", "thu", "fri", "sat", "sun"]
    start_day = 5  # 9th September 2017 is Saturday
    return days[(start_day + X - 1) % 7]