def check_rotation():
    grid = [input(), input()]
    
    if grid[0][::-1] == grid[1][::-1]:
        print("YES")
    else:
        print("NO") 

check_rotation()