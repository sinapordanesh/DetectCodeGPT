def calculate_happiness_points(X):
    num_500_yen_coins = X // 500
    remaining_yen = X % 500
    
    happiness_points = num_500_yen_coins * 1000
    
    num_5_yen_coins = remaining_yen // 5
    happiness_points += num_5_yen_coins * 5
    
    return happiness_points

X = int(input())
print(calculate_happiness_points(X))