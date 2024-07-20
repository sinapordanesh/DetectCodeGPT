def card_operations(N, cards):
    ans = [0] * N
    count_dict = {}
    
    for i in range(N):
        if cards[i] in count_dict:
            count_dict[cards[i]] += 1
        else:
            count_dict[cards[i]] = 1

    for key, value in count_dict.items():
        ans[value - 1] += 1

    return ans

# Sample Input 1
print(card_operations(3, [2, 1, 2])) 

# Sample Input 2
print(card_operations(5, [1, 2, 3, 4, 5])) 

# Sample Input 3
print(card_operations(4, [1, 3, 3, 3])) 