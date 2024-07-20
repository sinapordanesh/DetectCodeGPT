def max_pairs(cards):
    m, n, *nums = cards
    b_nums = nums[:m]
    r_nums = nums[m:]
    
    pairs = 0
    while b_nums and r_nums:
        max_pairs = 0
        for b_num in b_nums:
            for r_num in r_nums:
                if math.gcd(b_num, r_num) > 1:
                    max_pairs += 1
        pairs += max_pairs
        
        b_nums = [b_num for b_num in b_nums if not any(math.gcd(b_num, r_num) > 1 for r_num in r_nums)]
        r_nums = [r_num for r_num in r_nums if not any(math.gcd(b_num, r_num) > 1 for b_num in b_nums)]
        
    return pairs

import math

# Input
datasets = []
while True:
    data = list(map(int, input().split()))
    if data == [0, 0]:
        break
    datasets.append(data)

# Output
for data in datasets:
    result = max_pairs(data)
    print(result)