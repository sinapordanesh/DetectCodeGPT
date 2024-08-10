def automaton_states(N, M, A, B, C, T, initial_states):
    def next_state(i, t):
        if i < 0 or i >= N:
            return 0
        return (A * initial_states[i-1] + B * initial_states[i] + C * initial_states[i+1]) % M
    
    for _ in range(T):
        new_states = [next_state(i, 0) for i in range(N)]
        initial_states = new_states

    return new_states

# Sample Input
print(automaton_states(5, 4, 1, 3, 2, 0, [0, 1, 2, 0, 1]))
print(automaton_states(5, 7, 1, 3, 2, 1, [0, 1, 2, 0, 1]))
print(automaton_states(5, 13, 1, 3, 2, 11, [0, 1, 2, 0, 1]))
print(automaton_states(5, 5, 2, 0, 1, 100, [0, 1, 2, 0, 1]))
print(automaton_states(6, 6, 0, 2, 3, 1000, [0, 1, 2, 0, 1, 4]))
print(automaton_states(20, 1000, 0, 2, 3, 1000000000, [0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1, 0, 1, 2, 0, 1]))
print(automaton_states(30, 2, 1, 0, 1, 1000000000, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(automaton_states(30, 2, 1, 1, 1, 1000000000, [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))
print(automaton_states(30, 5, 2, 3, 1, 1000000000, [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]))