def print_properties_of_binary_heap(H, values):
    for i in range(1, H + 1):
        parent_idx = i // 2
        left_child_idx = 2 * i
        right_child_idx = 2 * i + 1
        
        properties = f"node {i}: key = {values[i - 1]}, "
        
        if parent_idx >= 1:
            properties += f"parent key = {values[parent_idx - 1]}, "
        
        if left_child_idx <= H:
            properties += f"left key = {values[left_child_idx - 1]}, "
        
        if right_child_idx <= H:
            properties += f"right key = {values[right_child_idx - 1]}, "
        
        print(properties)

# Sample Input
H = 5
values = [7, 8, 1, 2, 3]

# Sample Output
print_properties_of_binary_heap(H, values)