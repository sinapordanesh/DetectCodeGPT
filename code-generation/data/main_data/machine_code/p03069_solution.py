def min_recolor_stones(N, S):
    count = 0
    for i in range(N-1):
        if S[i] == "." and S[i+1] == "#":
            count += 1
    return count

#Sample Input
N = 3
S = "#.#"
print(min_recolor_stones(N, S))

N = 5
S = "#.##."
print(min_recolor_stones(N, S))

N = 9
S = "........."
print(min_recolor_stones(N, S))