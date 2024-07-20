def find_kth_lunlun_number(K):
    lunlun_numbers = [1]
    while len(lunlun_numbers) < K:
        for i in range(len(lunlun_numbers)):
            x = lunlun_numbers[i]
            last_digit = x % 10
            if last_digit > 0:
                lunlun_numbers.append(10*x + last_digit - 1)
            lunlun_numbers.append(10*x + last_digit)
            if last_digit < 9:
                lunlun_numbers.append(10*x + last_digit + 1)
    return lunlun_numbers[K-1]

K = int(input())
print(find_kth_lunlun_number(K))