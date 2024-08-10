def max_early_wakeups(N, records):
    total_seconds = 0
    early_wakeups = 0
    for i in range(N):
        total_seconds += records[i][0] + records[i][1]
        if total_seconds >= 10800 and total_seconds < 32400:
            early_wakeups += 1
        if total_seconds >= 86400:
            total_seconds = 0
    return early_wakeups

# Sample Input 1
print(max_early_wakeups(3, [[28800, 57600], [28800, 57600], [57600, 28800]]))

# Sample Input 2
print(max_early_wakeups(10, [[28800, 57600], [4800, 9600], [6000, 1200], [600, 600], [300, 600], [5400, 600], [6000, 5760], [6760, 2880], [6000, 12000], [9000, 600]]))