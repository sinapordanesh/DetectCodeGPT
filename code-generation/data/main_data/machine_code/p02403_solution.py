def print_rectangle(H, W):
    for i in range(H):
        print('#' * W)
    print()

# Read input
while True:
    H, W = map(int, input().split())
    if H == 0 and W == 0:
        break
    print_rectangle(H, W)