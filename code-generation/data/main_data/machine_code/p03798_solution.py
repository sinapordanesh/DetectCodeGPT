def animal_assignment(N, s):
    animals = [''] * N
    
    if s[0] == 'o':
        animals[0] = 'S'
        animals[1] = 'S' if s[1] == 'o' else 'W'
    else:
        animals[0] = 'W'
        animals[1] = 'S' if s[1] == 'x' else 'W'
    
    for i in range(2, N):
        if s[i] == 'o':
            if animals[i-1] == 'S':
                animals[i] = 'S'
            else:
                animals[i] = 'W'
        else:
            if animals[i-1] == 'S':
                animals[i] = 'W'
            else:
                animals[i] = 'S'
    
    if s[N-1] == 'o':
        if animals[N-1] == animals[0] and animals[N-1] == animals[N-2]:
            return ''.join(animals)
        else:
            return -1
    else:
        if animals[N-1] != animals[0] and animals[N-1] != animals[N-2]:
            return ''.join(animals)
        else:
            return -1

# Test the function with the provided samples
print(animal_assignment(6, "ooxoox"))
print(animal_assignment(3, "oox"))
print(animal_assignment(10, "oxooxoxoox"))