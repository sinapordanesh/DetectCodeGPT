def dial_lock(k, initial, unlocking):
    count = 0
    for i in range(k):
        diff = abs(int(initial[i]) - int(unlocking[i]))
        count += min(diff, 10 - diff)
    return count

while True:
    k = int(input())
    if k == 0:
        break
    initial, unlocking = input().split()
    print(dial_lock(k, initial, unlocking))