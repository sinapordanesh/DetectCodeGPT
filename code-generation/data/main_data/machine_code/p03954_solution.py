def find_integer_written(N, a):
    nums = [0] * (2*N)
    nums[0] = a[0]
    
    for i in range(1, 2*N-1):
        nums[i] = a[i]
        if i % 2 == 1:
            nums[i] = max(nums[i], min(nums[i-1], a[i-1]))
        else:
            nums[i] = max(nums[i], min(nums[i-1], a[i+1]))
    
    return nums[-1]

N = 4
a = [1, 6, 3, 7, 4, 5, 2]
print(find_integer_written(N, a))

N = 2
a = [1, 2, 3]
print(find_integer_written(N, a))