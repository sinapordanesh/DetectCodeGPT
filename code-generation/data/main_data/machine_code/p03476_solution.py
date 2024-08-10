def similar_to_2017(Q, queries):
    def is_prime(num):
        if num < 2:
            return False
        for i in range(2, int(num ** 0.5) + 1):
            if num % i == 0:
                return False
        return True

    def similar_count(l, r):
        count = 0
        for x in range(l, r+1):
            if is_prime(x) and is_prime((x + 1) // 2):
                count += 1
        return count

    result = []
    for query in queries:
        l, r = query
        result.append(similar_count(l, r))
    
    return result

# Sample Input 1
Q1 = 1
queries1 = [(3, 7)]
print(similar_to_2017(Q1, queries1))

# Sample Input 2
Q2 = 4
queries2 = [(13, 13), (7, 11), (7, 11), (2017, 2017)]
print(similar_to_2017(Q2, queries2))

# Sample Input 3
Q3 = 6
queries3 = [(1, 53), (13, 91), (37, 55), (19, 51), (73, 91), (13, 49)]
print(similar_to_2017(Q3, queries3))