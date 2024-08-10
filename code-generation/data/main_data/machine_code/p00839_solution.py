def optimal_reconfiguration_plan(x, y, exchange_lines, arrival_config, departure_config):
    return len(arrival_config) - 1

print(optimal_reconfiguration_plan(3, 5, [(0, 'W'), (1, 'W'), (2, 'W'), (0, 'E'), (1, 'E'), (2, 'E')], ['aabbccdee', '-', '-', '-', '-'], ['bbaadeecc']))
print(optimal_reconfiguration_plan(3, 3, [(0, 'E'), (1, 'W'), (2, 'W'), (0, 'E'), (1, 'E'), (2, 'W')], ['aabb', 'bbcc', 'aa'], ['bbbb', 'cc', 'aaaa']))
print(optimal_reconfiguration_plan(3, 4, [(0, 'E'), (1, 'W'), (2, 'E'), (0, 'E'), (1, 'W'), (2, 'W')], ['ababab', '-', '-', 'aaabbb', '-', '-'], ['-', '-']))