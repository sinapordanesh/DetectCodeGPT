def sort_three_numbers():
    nums = list(map(int, input().split()))
    nums.sort()
    print(*nums)

sort_three_numbers()