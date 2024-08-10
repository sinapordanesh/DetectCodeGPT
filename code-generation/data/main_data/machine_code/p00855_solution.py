def prime_gap_length(k):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def find_next_prime(num):
        while True:
            num += 1
            if is_prime(num):
                return num

    while k != 0:
        if is_prime(k) or k == 1:
            print(0)
        else:
            lower_prime = k
            while not is_prime(lower_prime):
                lower_prime -= 1
            upper_prime = find_next_prime(k)
            gap_length = upper_prime - lower_prime - 1
            print(gap_length)
        k = int(input())

prime_gap_length(int(input()))