def enumeration_of_subsets(n, k, b):
    def subsets_helper(nums, path, res, index):
        res.append(path)
        for i in range(index, len(nums)):
            subsets_helper(nums, path + [nums[i]], res, i + 1)
    
    nums = [1 << i for i in range(n)]
    target = sum([nums[i] for i in b])
    
    res = []
    subsets_helper(nums, [], res, 0)
    
    for subset in res:
        if sum(subset) & target == target:
            print(f"{sum(subset)}:", end=" ")
            for num in subset:
                if num in nums:
                    print(nums.index(num), end=" ")
            print()

n = 4
k = 2
b = [0, 2]
enumeration_of_subsets(n, k, b)