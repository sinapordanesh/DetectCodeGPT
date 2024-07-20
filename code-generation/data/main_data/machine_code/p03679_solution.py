def food_condition(X, A, B):
    if B <= A:
        return "delicious"
    elif B - A <= X:
        return "safe"
    else:
        return "dangerous" 

X, A, B = map(int, input().split())
print(food_condition(X, A, B))