def rearrange_sequence(n, m, requests):
    sequence = list(range(1, n + 1))
    
    for request in requests:
        sequence.remove(request)
        sequence.insert(0, request)
    
    return sequence

# Sample Input 1
n1 = 5
m1 = 3
requests1 = [4, 2, 5]
print(*rearrange_sequence(n1, m1, requests1))

# Sample Input 2
n2 = 10
m2 = 8
requests2 = [1, 4, 7, 3, 4, 10, 1, 3]
print(*rearrange_sequence(n2, m2, requests2))