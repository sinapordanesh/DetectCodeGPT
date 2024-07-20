def S(n):
    return sum(int(i) for i in str(n))

def smallest_snuke_numbers(K):
    result = []
    n = 1
    while len(result) < K:
        if all(n / S(n) <= m / S(m) for m in range(n+1, n+10)):
            result.append(n)
        n += 1
    return result

K = int(input())
for num in smallest_snuke_numbers(K):
    print(num)