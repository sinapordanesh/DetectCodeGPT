def good_string(w):
    best_representations = [w]
    num_elements = 1
    num_best_representations = 1
    
    for i in range(1, len(w)):
        if w[:i] != w[i:]:
            best_representations.append((w[:i], w[i:]))
            num_elements = 2
            num_best_representations += 1
    
    print(num_elements)
    print(num_best_representations)

# Test the function with the provided sample inputs
good_string("aab")
good_string("bcbc")
good_string("ddd")