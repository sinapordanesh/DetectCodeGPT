def max_satisfaction(N, K, sushi):
    sushi.sort(key=lambda x: x[1], reverse=True)
    kind_dict = {}
    total_deliciousness = 0
    variety = 0
    result = 0
    
    for i in range(K):
        total_deliciousness += sushi[i][1]
        if sushi[i][0] not in kind_dict:
            kind_dict[sushi[i][0]] = 1
            variety += 1
        else:
            kind_dict[sushi[i][0]] += 1
    
    result = total_deliciousness + variety**2
    
    return result

# Sample Input 1
N = 5
K = 3
sushi = [(1, 9), (1, 7), (2, 6), (2, 5), (3, 1)]
print(max_satisfaction(N, K, sushi))

# Sample Input 2
N = 7
K = 4
sushi = [(1, 1), (2, 1), (3, 1), (4, 6), (4, 5), (4, 5), (4, 5)]
print(max_satisfaction(N, K, sushi))

# Sample Input 3
N = 6
K = 5
sushi = [(5, 1000000000), (2, 990000000), (3, 980000000), (6, 970000000), (6, 960000000), (4, 950000000)]
print(max_satisfaction(N, K, sushi))