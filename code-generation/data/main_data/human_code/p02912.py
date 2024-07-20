def input_int():
    return(int(input()))

def input_int_list():
    return(list(map(int,input().split())))

def input_int_map():
    return(map(int,input().split()))

import heapq

def run():
    n, ticket_count = input_int_map()

    nums = input_int_list()


    nums = list(map(lambda x: x * (-1), nums))  # 各要素を-1倍

    heapq.heapify(nums)



    for _ in range(ticket_count):
        num = (heapq.heappop(nums) * (-1))

        num = num // 2

        heapq.heappush(nums, num * (-1))

    nums = list(map(lambda x: x * (-1), nums))
    print(sum(nums))

run()

# 2 4 3

# 3 4 3

# 2 6 3















