def animals_in_garden(X, Y):
    for num_turtles in range(0, X+1):
        num_cranes = X - num_turtles
        total_legs = num_turtles * 4 + num_cranes * 2
        if total_legs == Y:
            return "Yes"
    return "No" 

X, Y = map(int, input().split())
print(animals_in_garden(X, Y))