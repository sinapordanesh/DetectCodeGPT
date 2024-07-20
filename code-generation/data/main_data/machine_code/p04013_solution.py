def num_ways(N, A, cards):
    def dfs(index, total, count):
        if index == N:
            if count > 0 and total / count == A:
                return 1
            else:
                return 0
        return dfs(index + 1, total + cards[index], count + 1) + dfs(index + 1, total, count)

    return dfs(0, 0, 0)

# Sample Input 1
print(num_ways(4, 8, [7, 9, 8, 9]))

# Sample Input 2
print(num_ways(3, 8, [6, 6, 9]))

# Sample Input 3
print(num_ways(8, 5, [3, 6, 2, 8, 7, 6, 5, 9]))

# Sample Input 4
print(num_ways(33, 3, [3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3, 3]))