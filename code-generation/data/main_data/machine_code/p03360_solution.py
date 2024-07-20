def largest_possible_sum(A, B, C, K):
    nums = [A, B, C]
    for _ in range(K):
        max_num_index = nums.index(max(nums))
        nums[max_num_index] *= 2
    return sum(nums)