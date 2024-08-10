def max_nutrition_balance(N, C, sushi):
    total_calories = 0
    max_balance = 0
    left_calories = [0] * (N+1)
    right_calories = [0] * (N+1)
    for i in range(N):
        total_calories += sushi[i][1]
        left_calories[i+1] = total_calories - sushi[i][0]
    total_calories = 0
    for i in range(N-1, -1, -1):
        total_calories += sushi[i][1]
        right_calories[i] = total_calories - (C - sushi[i][0])
    for i in range(N):
        balance = max(left_calories[i], right_calories[i])
        max_balance = max(max_balance, balance)
    return max_balance