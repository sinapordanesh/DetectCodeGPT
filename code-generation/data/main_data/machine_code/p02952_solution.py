def odd_number_of_digits(N):
    count = 0
    for i in range(1, N+1):
        if len(str(i)) % 2 == 1:
            count += 1
    return count

N = int(input())
print(odd_number_of_digits(N))