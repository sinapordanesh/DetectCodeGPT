def monster_battle(A, B, C, D):
    while True:
        C -= B
        if C <= 0:
            return "Yes"
        
        A -= D
        if A <= 0:
            return "No"

A, B, C, D = map(int, input().split())
print(monster_battle(A, B, C, D))