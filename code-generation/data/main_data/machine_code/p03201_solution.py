def max_pairs(N, balls):
    counts = {}
    for num in balls:
        counts[num] = counts.get(num, 0) + 1
    
    max_pairs = 0
    for num in counts:
        for i in range(32):
            target = 2**i - num
            if target in counts and (target != num or counts[num] > 1):
                pairs = min(counts[num], counts[target])
                max_pairs = max(max_pairs, pairs)
    
    return max_pairs

#Sample Input 1
print(max_pairs(3, [1, 2, 3]))

#Sample Input 2
print(max_pairs(5, [3, 11, 14, 5, 13]))