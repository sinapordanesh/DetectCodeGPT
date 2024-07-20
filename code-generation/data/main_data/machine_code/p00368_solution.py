def checkered_pattern(W, H, squares):
    def check_pattern(arr):
        for i in range(len(arr)-1):
            if arr[i] == arr[i+1]:
                return False
        return True
    
    rows = [check_pattern(row) for row in squares]
    cols = [check_pattern([squares[i][j] for i in range(H)]) for j in range(W)]
    
    if all(rows) and all(cols):
        return "yes"
    else:
        return "no"