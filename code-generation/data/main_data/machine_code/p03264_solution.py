def number_of_ways_to_choose_pair(K):
    count = K // 2
    return count * (K - count) 

K = int(input())
print(number_of_ways_to_choose_pair(K))