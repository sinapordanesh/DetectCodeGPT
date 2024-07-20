def red_ball_boxes(N, M, operations):
    boxes = [1] + [0] * (N - 1)
    red_boxes = {1}
    
    for x, y in operations:
        boxes[x - 1] -= 1
        boxes[y - 1] += 1
        
        if x in red_boxes:
            red_boxes.add(y)
            if boxes[x - 1] == 0:
                red_boxes.remove(x)
    
    return len(red_boxes)