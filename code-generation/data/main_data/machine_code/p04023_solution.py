def integer_sequence(N, Q, operations):
    current_sequence = list(range(1, N+1))
    
    for q in operations:
        new_sequence = []
        total_length = sum(q)
        num_full_sequences = total_length // N
        remaining_elements = total_length % N
        
        for i in range(num_full_sequences):
            new_sequence += current_sequence
        
        new_sequence += current_sequence[:remaining_elements]
        current_sequence = new_sequence[:N]
    
    result = [current_sequence.count(i) for i in range(1, N+1)]
    
    for i in result:
        print(i)

# Sample Input 1
integer_sequence(5, 3, [6, 4, 11])

# Sample Input 2
integer_sequence(10, 10, [9, 13, 18, 8, 10, 10, 9, 19, 22, 27])