def minimum_operators_needed(datasets):
    for dataset in datasets:
        N, T = dataset[0]
        customers = dataset[1:]
        max_stand_by = max(customer[1] for customer in customers)
        operators = 0
        time_passed = 0
        while customers:
            busy_operators = []
            for i, customer in enumerate(customers):
                if time_passed <= customer[1]:
                    busy_operators.append(customer)
                    customers.pop(i)
            if not busy_operators:
                busy_operators.append(customers.pop(0))
                
            operators += 1
            time_passed += max_stand_by
            for customer in busy_operators:
                time_passed += customer[0]
                
        print(operators)