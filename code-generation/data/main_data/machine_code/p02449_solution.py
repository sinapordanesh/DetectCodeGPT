def permutation(n, arr):
    def prev_permutation(arr):
        i = len(arr) - 1
        while i > 0 and arr[i-1] <= arr[i]:
            i -= 1
        if i <= 0:
            return None
        
        j = len(arr) - 1
        while arr[j] >= arr[i-1]:
            j -= 1
        
        arr[i-1], arr[j] = arr[j], arr[i-1]
        
        arr[i:] = arr[len(arr)-1:i-1:-1]
        
        return arr
    
    def next_permutation(arr):
        i = len(arr) - 1
        while i > 0 and arr[i-1] >= arr[i]:
            i -= 1
        if i <= 0:
            return None
        
        j = len(arr) - 1
        while arr[j] <= arr[i-1]:
            j -= 1
        
        arr[i-1], arr[j] = arr[j], arr[i-1]
        
        arr[i:] = arr[len(arr)-1:i-1:-1]
        
        return arr
    
    prev = prev_permutation(arr.copy())
    next = next_permutation(arr.copy())
    
    if prev:
        print(' '.join(map(str, prev)))
    print(' '.join(map(str, arr)))
    if next:
        print(' '.join(map(str, next)))

n = 3
arr = [2, 1, 3]
permutation(n, arr)

n = 3
arr = [3, 2, 1]
permutation(n, arr)