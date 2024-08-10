def lagrange_four_square(input_list):
    def num_representations(n):
        dp = [0] * (n + 1)
        dp[0] = 1

        for i in range(1, int(n ** 0.5) + 1):
            square = i * i
            for j in range(square, n + 1):
                dp[j] += dp[j - square]

        return dp[n]

    result = []
    for num in input_list:
        if num == 0:
            break
        result.append(num_representations(num))

    return result

input_list = [1, 25, 2003, 211, 20007, 0]
output = lagrange_four_square(input_list)
for o in output:
    print(o)