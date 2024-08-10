def takahashi_days(a, b):
    count = 0
    for i in range(1, min(a, b) + 1):
        count += 1
    return count

print(takahashi_days(5, 5))