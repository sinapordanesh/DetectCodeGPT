N = int(input())
A = list(map(int,input().split()))

import math

def gcd_list(nums):
  gcd = nums[0]
  for i in range(1,len(nums)):
    gcd = math.gcd(gcd,nums[i])
  return gcd

print(gcd_list(A))