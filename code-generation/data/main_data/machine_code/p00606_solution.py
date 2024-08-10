def cleaning_robot_probability(n, s, t, b):
    if n == 0:
        return
    
    def move_robot(curr_room, battery):
        if curr_room == b or battery == 0:
            return 0
        elif curr_room == t:
            return 1
        
        next_rooms = {
            'A': ['B', 'D'],
            'B': ['A', 'C', 'E'],
            'C': ['B', 'F'],
            'D': ['A', 'E', 'G'],
            'E': ['B', 'D', 'F', 'H'],
            'F': ['C', 'E', 'I'],
            'G': ['D', 'H'],
            'H': ['E', 'G', 'I'],
            'I': ['F', 'H']
        }
        
        prob = 0
        for next_room in next_rooms[curr_room]:
            prob += 0.25 * move_robot(next_room, battery - 1)
        
        return prob
    
    probability = move_robot(s, n)
    print('%.8f' % probability)

# Test the function with sample input
cleaning_robot_probability(1, 'E', 'A', 'C')
cleaning_robot_probability(1, 'E', 'B', 'C')
cleaning_robot_probability(2, 'E', 'A', 'B')