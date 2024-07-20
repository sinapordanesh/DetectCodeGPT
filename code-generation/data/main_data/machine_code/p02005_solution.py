def colorful_drink():
    N = int(input())
    liquids = {}
    for _ in range(N):
        color, density = input().split()
        density = int(density)
        if color not in liquids or density < liquids[color]:
            liquids[color] = density
            
    M = int(input())
    drink = []
    for _ in range(M):
        drink.append(input())
        
    valid = True
    for i in range(1, len(drink)):
        if drink[i] not in liquids or drink[i-1] not in liquids or liquids[drink[i]] >= liquids[drink[i-1]]:
            valid = False
            break
            
    if valid:
        print('Yes')
    else:
        print('No')

colorful_drink()