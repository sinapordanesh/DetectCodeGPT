def average_beauty(n, m, d):
    total_beauty = 0
    total_sequences = n ** m
    
    for i in range(n):
        total_beauty += ((n - abs(i - d)) * (n - abs(i + d)))
    
    return total_beauty / total_sequences

n, m, d = map(int, input().split())
print("{:.10f}".format(average_beauty(n, m, d)))