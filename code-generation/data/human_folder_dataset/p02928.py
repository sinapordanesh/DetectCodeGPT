def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))

def run():

    n, k = input_int_map()

    nums = input_int_list()


    in_list_count = 0
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if nums[i] > nums[j]:
                in_list_count += 1

    in_list_count_sum = in_list_count * k

    other_list_count = 0

    for num in nums:
        for num2 in nums:
            if num > num2:
                other_list_count += 1


    other_list_count_sum = other_list_count * k * (k - 1) // 2

    result = (in_list_count_sum + other_list_count_sum) % (10 ** 9 + 7)
    print(result)

run()

# RRLRL
# 0 2 1 1 1

# 1 1 2 2 0


















