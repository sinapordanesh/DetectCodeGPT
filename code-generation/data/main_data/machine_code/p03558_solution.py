def smallest_possible_sum(K):
    n = 1
    while True:
        if (n*K) % 10 == 0 or (n*K) % 10 == K:
            return n
        n += 1
        
K = int(input())
print(smallest_possible_sum(K))