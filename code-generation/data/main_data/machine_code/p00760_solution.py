def calculate_days(n, datasets):
    result = []
    for data in datasets:
        Y, M, D = data
        days = 0
        for year in range(Y, 1000):
            if year % 3 == 0:
                days += 10 * 20
            else:
                for month in range(1, 11):
                    if month % 2 == 0:
                        days += 19
                    else:
                        days += 20
        days -= D
        if M % 2 == 0:
            days -= 19 * (11 - M)
        else:
            days -= 20 * (11 - M)
        result.append(days)
    return result