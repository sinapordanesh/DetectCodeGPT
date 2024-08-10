def max_total_value(N, items, Q, queries):
    def max_value(v, L):
        ans = 0
        while v > 0:
            dp = [0] * (L + 1)
            for i in range(1, L + 1):
                dp[i] = dp[i - 1]
                if i >= items[v-1][1]:
                    dp[i] = max(dp[i], dp[i - items[v-1][1]] + items[v-1][0])
            ans = max(ans, dp[L])
            v //= 2
        return ans

    result = []
    for i in range(Q):
        result.append(max_value(queries[i][0], queries[i][1]))

    return result

# Sample Input 1
N = 3
items = [(1, 2), (2, 3), (3, 4)]
Q = 3
queries = [(1, 1), (2, 5), (3, 5)]
print(max_total_value(N, items, Q, queries))

# Sample Input 2
N = 15
items = [(123, 119), (129, 120), (132, 112), (126, 109), (118, 103), (115, 109), (102, 100), (130, 120), (105, 105), (132, 115), (104, 102), (107, 107), (127, 116), (121, 104), (121, 115)]
Q = 8
queries = [(8, 234), (9, 244), (10, 226), (11, 227), (12, 240), (13, 237), (14, 206), (15, 227)]
print(max_total_value(N, items, Q, queries))