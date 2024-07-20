def longest_arithmetic_progression(n, nums):
    nums = set(nums)
    longest = 2
    
    for i in range(n):
        for j in range(i+1, n):
            a, b = nums[i], nums[j]
            d = b - a
            curr = 2
            while a - d in nums:
                a -= d
                curr += 1
            longest = max(longest, curr)
    
    return longest