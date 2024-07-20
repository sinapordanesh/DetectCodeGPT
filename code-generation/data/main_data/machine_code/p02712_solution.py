def fizzbuzz_sum(N):
    total = 0
    for i in range(1, N+1):
        if i % 3 == 0 and i % 5 == 0:
            total += i
        elif i % 3 == 0:
            total += i
        elif i % 5 == 0:
            total += i
    return total

N = int(input())
print(fizzbuzz_sum(N))