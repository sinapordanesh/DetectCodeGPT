def bozosort(N, arr, Q, commands):
    def is_sorted(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))
    
    def bozosort_helper(arr):
        count = 0
        while not is_sorted(arr):
            i, j = random.sample(range(len(arr)), 2)
            arr[i], arr[j] = arr[j], arr[i]
            count += 1
        return count
    
    import random
    
    for x, y in commands:
        arr[x-1], arr[y-1] = arr[y-1], arr[x-1]
        result = bozosort_helper(arr)
        if is_sorted(arr):
            return result + 1
    return -1