def count_combinations(N, M, switches, bulbs):
    def light_bulb(bulb, switch_states):
        count = 0
        for i in range(len(bulbs[bulb][:-1])):
            num_on = sum([switch_states[switch-1] for switch in bulbs[bulb][:-1]])
            if num_on % 2 == bulbs[bulb][-1]:
                count += 1
        return count

    def backtrack(curr_bulb, switch_states):
        if curr_bulb == M:
            return light_bulb(curr_bulb, switch_states)
        
        count = 0
        for state in [0, 1]:
            switch_states_copy = switch_states.copy()
            switch_states_copy[curr_bulb] = state
            count += backtrack(curr_bulb + 1, switch_states_copy)
        
        return count
    
    return backtrack(0, [0] * N)