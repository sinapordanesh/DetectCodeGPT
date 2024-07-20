def count_multiples(L, R, d):
    count = 0
    for i in range(L, R+1):
        if i % d == 0:
            count += 1
    return count

L, R, d = map(int, input().split())
print(count_multiples(L, R, d))