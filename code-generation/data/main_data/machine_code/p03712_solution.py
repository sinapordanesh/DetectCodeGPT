def draw_box(image):
    H, W = map(int, image[0].split())
    image = image[1:]
    
    result = ['#' * (W + 2)]
    for row in image:
        result.append('#' + row + '#')
    result.append('#' * (W + 2))
    
    for line in result:
        print(line)

# Sample Input 1
image1 = ["2 3", "abc", "arc"]
draw_box(image1)

# Sample Input 2
image2 = ["1 1", "z"]
draw_box(image2)