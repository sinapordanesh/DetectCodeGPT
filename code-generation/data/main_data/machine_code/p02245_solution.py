def min_steps_to_solve_puzzle(puzzle):
    initial_state = [int(num) for num in puzzle.split()]
    goal_state = [1, 2, 3, 4, 5, 6, 7, 8, 0]
    steps = 0
    
    while initial_state != goal_state:
        zero_idx = initial_state.index(0)
        if initial_state[zero_idx - 3] == 0:
            initial_state[zero_idx - 3], initial_state[zero_idx] = initial_state[zero_idx], initial_state[zero_idx - 3]
            steps += 1
        elif initial_state[zero_idx + 3] == 0:
            initial_state[zero_idx + 3], initial_state[zero_idx] = initial_state[zero_idx], initial_state[zero_idx + 3]
            steps += 1
        elif initial_state[zero_idx - 1] == 0:
            initial_state[zero_idx - 1], initial_state[zero_idx] = initial_state[zero_idx], initial_state[zero_idx - 1]
            steps += 1
        elif initial_state[zero_idx + 1] == 0:
            initial_state[zero_idx + 1], initial_state[zero_idx] = initial_state[zero_idx], initial_state[zero_idx + 1]
            steps += 1
                
    return steps

# Sample Input
puzzle = "1 3 0 4 2 5 7 8 6"
print(min_steps_to_solve_puzzle(puzzle))