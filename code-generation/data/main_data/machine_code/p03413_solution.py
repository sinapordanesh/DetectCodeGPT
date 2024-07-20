def maximize_final_element(N, sequence):
    operations = []
    
    while len(sequence) > 1:
        if sequence[0] >= sequence[-1]:
            operations.append(1)
            sequence = sequence[1:]
        else:
            operations.append(len(sequence))
            sequence = sequence[:-1]
    
    final_value = sum(sequence)
    
    print(final_value)
    print(len(operations))
    for operation in operations:
        print(operation)