def compute_debt(n):
    debt = 100000
    for i in range(n):
        interest = debt * 0.05
        debt += interest
        debt = round(debt, -3)
    return debt

n = int(input())
print(compute_debt(n))