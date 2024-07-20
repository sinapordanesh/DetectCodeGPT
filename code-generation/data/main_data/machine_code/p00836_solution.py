def prime_number(num):
    primes = []
    for i in range(2, num):
        for j in range(2, i):
            if i % j == 0:
                break
        else:
            primes.append(i)
    
    count = 0
    for i in range(len(primes)):
        total = 0
        for j in range(i, len(primes)):
            total += primes[j]
            if total == num:
                count += 1
            if total > num:
                break
    
    return count

while True:
    num = int(input())
    if num == 0:
        break
    print(prime_number(num))