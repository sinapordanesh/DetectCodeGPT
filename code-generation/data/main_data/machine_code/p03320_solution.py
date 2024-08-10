def is_snuke_number(n):
    def sum_of_digits(num):
        return sum([int(x) for x in str(num)])
    
    for m in range(n+1, 10**15+1):
        if (n / sum_of_digits(n)) > (m / sum_of_digits(m)):
            return False
    return True

def list_snuke_numbers(K):
    snuke_numbers = []
    num = 1
    while len(snuke_numbers) < K:
        if is_snuke_number(num):
            snuke_numbers.append(num)
        num += 1
    return snuke_numbers

K = 10
for num in list_snuke_numbers(K):
    print(num)