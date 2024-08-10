def where_is_the_boundary(n, m, data):
    errors = [sum([1 for i in range(n) if data[j][i] == 'W']) for j in range(m)]
    
    min_error = float('inf')
    boundary = (1, 2)
    
    for i in range(1, n):
        error = sum(errors[0:i]) + sum([m - errors[j] for j in range(i, m)])
        if error < min_error:
            min_error = error
            boundary = (i, i + 1)
    
    return boundary

# Sample Input
print(where_is_the_boundary(2, 1, ['WE']))
print(where_is_the_boundary(3, 2, ['WWE', 'WEE']))
print(where_is_the_boundary(3, 1, ['WWW']))
print(where_is_the_boundary(3, 1, ['WEW']))