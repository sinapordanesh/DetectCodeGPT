def extend_image():
    H, W = map(int, input().split())
    image = []
    for _ in range(H):
        image.append(input())
    
    for row in image:
        print(row)
        print(row)

extend_image()