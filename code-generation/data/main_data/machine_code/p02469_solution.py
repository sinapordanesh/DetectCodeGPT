def least_common_multiple(n, nums):
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a
    
    def lcm(a, b):
        return abs(a*b) // gcd(a, b)
    
    ans = nums[0]
    for i in range(1, n):
        ans = lcm(ans, nums[i])
    
    return ans

# Sample Input 1
print(least_common_multiple(3, [3, 4, 6])) # Output: 12

# Sample Input 2
print(least_common_multiple(4, [1, 2, 3, 5])) # Output: 30