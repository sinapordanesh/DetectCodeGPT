def build_pyramid(N, x):
    if x == 1 or x == 2*N-1:
        print("No")
    else:
        print("Yes")
        print(x)
        nums = [i for i in range(1, 2*N-1) if i != x]
        mid = len(nums) // 2
        for i in range(mid):
            print(nums[i])
            print(nums[mid+i])
        if len(nums) % 2 != 0:
            print(nums[-1])

# Test the function
build_pyramid(4, 4)