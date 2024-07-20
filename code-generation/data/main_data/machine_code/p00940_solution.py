def deadlock_detection(p, r, t, resources, needs, logs):
    
    available = resources.copy()
    allocation = [[0]*r for _ in range(p)]
    
    for log in logs:
        idx = log[0] - 1
        resource_type = log[1] - 1
        allocation[idx][resource_type] += 1
        available[resource_type] -= 1

        possible = True
        while possible:
            possible = False
            for i in range(p):
                if allocation[i] == needs[i]:
                    continue
                can_allocate = True
                for j in range(r):
                    if needs[i][j] - allocation[i][j] > available[j]:
                        can_allocate = False
                        break
                if can_allocate:
                    for j in range(r):
                        available[j] += allocation[i][j]
                        allocation[i][j] = 0
                    possible = True
    
    return -1