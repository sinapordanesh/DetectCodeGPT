def max_lunch_boxes(data):
    for dataset in data:
        n, m = dataset[0], dataset[1]
        recipes = dataset[2:]
        ingredients = set()
        count = 0
        
        for recipe in recipes:
            ingredients.add(recipe)
        
        for i in range(1, 2**n):
            box = set()
            for j in range(n):
                if i & (1 << j):
                    box = box.union(ingredients[j])
            
            if len(box) == m:
                count = max(count, bin(i).count('1'))
        
        print(count)