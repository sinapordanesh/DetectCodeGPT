def calculate_years(X):
    deposit = 100
    interest_rate = 0.01
    years = 0
    
    while deposit < X:
        deposit += int(deposit * interest_rate)
        years += 1
    
    return years

X = int(input())
print(calculate_years(X))