def shredding_company(target, num):
    def backtrack(nums, path, res):
        if sum(path) <= target:
            res.append(path.copy())
        if sum(path) > target:
            return
        for i in range(len(nums)):
            path.append(nums[i])
            backtrack(nums[i + 1:], path, res)
            path.pop()

    res = []
    backtrack(list(map(int, str(num))), [], res)
    if not res:
        print("error")
    elif len(res) > 1:
        print("rejected")
    else:
        print(sum(res[0]), *res[0])

# Sample Input
shredding_company(50, 12346)
shredding_company(376, 144139)
shredding_company(927438, 927438)
shredding_company(18, 3312)
shredding_company(9, 3142)
shredding_company(25, 1299)
shredding_company(111, 33333)
shredding_company(103, 862150)
shredding_company(6, 1104)