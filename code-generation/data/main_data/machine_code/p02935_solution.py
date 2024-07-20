import itertools

def max_possible_value(N, values):
    def get_max_value(ingredients):
        while len(ingredients) > 1:
            new_ingredient = [(x + y) / 2 for x, y in zip(ingredients, ingredients[1:])]
            ingredients = new_ingredient
        return ingredients[0]
    
    max_value = 0
    for comb in itertools.combinations(values, 2):
        remaining_values = [v for v in values if v not in comb]
        remaining_values.append(sum(comb) / 2)
        max_value = max(max_value, get_max_value(remaining_values))
    
    return max_value

# Read input values
N = int(input())
values = list(map(int, input().split()))

# Output the result
print(max_possible_value(N, values))