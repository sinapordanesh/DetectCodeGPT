def max_circles(N, arr):
    def is_cubic(x):
        return int(x ** (1/3)) ** 3 == x
        
    nums = set()
    squares = set()
    
    for num in arr:
        if any((num % s == 0) for s in squares):
            continue
        for n in nums:
            if is_cubic(n * num):
                squares.add(num)
                break
        else:
            nums.add(num)
    
    return len(nums) + len(squares)