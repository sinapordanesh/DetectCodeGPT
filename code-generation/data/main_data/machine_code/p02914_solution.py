def max_beauty(N, arr):
    result = 0
    for i in range(60):
        total = 0
        for num in arr:
            if num & (1 << i):
                total += 1
        result += (1 << i) * min(total, N-total)
    return result

# Sample Input 1
print(max_beauty(3, [3, 6, 5])) # 12

# Sample Input 2
print(max_beauty(4, [23, 36, 66, 65])) # 188

# Sample Input 3
print(max_beauty(20, [1008288677408720767, 539403903321871999, 1044301017184589821, 215886900497862655, 504277496111605629, 972104334925272829, 792625803473366909, 972333547668684797, 467386965442856573, 755861732751878143, 1151846447448561405, 467257771752201853, 683930041385277311, 432010719984459389, 319104378117934975, 611451291444233983, 647509226592964607, 251832107792119421, 827811265410084479, 864032478037725181])) # 2012721721873704572