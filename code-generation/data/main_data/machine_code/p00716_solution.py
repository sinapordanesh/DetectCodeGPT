def calculate_final_amount_of_fund(datasets):
    results = []
    for dataset in datasets:
        initial_amount = dataset[0]
        num_years = dataset[1]
        operations = dataset[3:]

        max_final_amount = 0
        for operation in operations:
            balance = initial_amount
            for _ in range(num_years):
                interest = balance * operation[1]
                if operation[0] == 1:  # Compound interest
                    balance += interest
                balance -= operation[2]

            final_amount = int(balance)
            if final_amount > max_final_amount:
                max_final_amount = final_amount

        results.append(max_final_amount)

    return results


# Sample input
datasets = [
    [1000000, 5, 2, [0, 0.03125, 3000], [1, 0.03125, 3000]],
    [6620000, 7, 2, [0, 0.0732421875, 42307], [1, 0.0740966796875, 40942]],
    [39677000, 4, 4, [0, 0.0709228515625, 30754], [1, 0.00634765625, 26165], [0, 0.03662109375, 79468], [0, 0.0679931640625, 10932]],
    [10585000, 6, 4, [1, 0.0054931640625, 59759], [1, 0.12353515625, 56464], [0, 0.0496826171875, 98193], [0, 0.0887451171875, 78966]]
]

# Output for the sample input
print(calculate_final_amount_of_fund(datasets))