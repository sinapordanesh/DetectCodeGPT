def can_collect_treasures():
    while True:
        n = int(input())
        if n == 0:
            break
        
        islands = []
        for _ in range(n):
            treasures, max_treasures = map(int, input().split())
            islands.append((treasures, max_treasures))
        
        total_treasures = sum(treasures for treasures, _ in islands)
        max_capacity = max(max_treasures for _, max_treasures in islands)
        
        if total_treasures <= max_capacity:
            print("Yes")
        else:
            print("No")

can_collect_treasures()