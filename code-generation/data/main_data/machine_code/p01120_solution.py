def tally_counters(n, m, initial_values, target_values):
    operations = 0
    for i in range(n):
        diff = abs(target_values[i] - initial_values[i])
        operations += min(diff, m - diff)
    return operations

while True:
    n, m = map(int, input().split())
    if n == 0 and m == 0:
        break
    initial_values = list(map(int, input().split()))
    target_values = list(map(int, input().split()))
    print(tally_counters(n, m, initial_values, target_values))