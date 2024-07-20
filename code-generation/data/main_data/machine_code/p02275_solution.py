def counting_sort(arr):
    k = max(arr) + 1
    count = [0] * k
    output = [0] * len(arr)
    
    for num in arr:
        count[num] += 1
    
    for i in range(1, k):
        count[i] += count[i-1]
    
    for num in reversed(arr):
        output[count[num]-1] = num
        count[num] -= 1
    
    return ' '.join(map(str, output))