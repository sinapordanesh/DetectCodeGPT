def count_odd_numbers_with_eight_divisors(N):
    def divisors_count(num):
        count = 0
        i = 1
        while i*i <= num:
            if num % i == 0:
                count += 2
                if i*i == num:
                    count -= 1
            i += 1
        return count

    count = 0
    for i in range(1, N+1):
        if i % 2 != 0 and divisors_count(i) == 8:
            count += 1
    print(count)

# Driver code
N = int(input())
count_odd_numbers_with_eight_divisors(N)