def dungeon_quest_HP(init_HP, max_HP, R, C, cave_info, trap_info, patrol_steps, potions):
    current_HP = init_HP
    for step in patrol_steps:
        direction, num_steps = step
        for _ in range(num_steps):
            if direction == 'U':
                R -= 1
            elif direction == 'D':
                R += 1
            elif direction == 'L':
                C -= 1
            elif direction == 'R':
                C += 1

            if R < 0 or R >= len(cave_info) or C < 0 or C >= len(cave_info[0]):
                return "NO"
            
            trap_type = cave_info[R][C]
            if trap_type in trap_info:
                current_HP -= trap_info[trap_type]
                if current_HP <= 0:
                    return "NO"
            
            if (R, C) in potions:
                current_HP = min(current_HP + potions[(R, C)], max_HP)
    
    return "YES"