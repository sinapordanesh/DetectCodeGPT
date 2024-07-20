def travel_cost(X, Y):
    return X + Y // 2

X, Y = map(int, input().split())
print(travel_cost(X, Y))