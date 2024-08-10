def shower_emit(N, T, *t):
    last_push = 0
    total_time = 0
    for i in t:
        if i - last_push >= T:
            total_time += T
        else:
            total_time += i - last_push
        last_push = i
    total_time += T
    return total_time

# Test the function with the sample inputs
print(shower_emit(2, 4, 0, 3)) # 7
print(shower_emit(2, 4, 0, 5)) # 8
print(shower_emit(4, 1000000000, 0, 1000, 1000000, 1000000000)) # 2000000000
print(shower_emit(1, 1, 0)) # 1
print(shower_emit(9, 10, 0, 3, 5, 7, 100, 110, 200, 300, 311)) # 67