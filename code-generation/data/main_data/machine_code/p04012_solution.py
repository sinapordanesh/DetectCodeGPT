def is_beautiful(w):
    freq = {}
    for char in w:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1
    
    for count in freq.values():
        if count % 2 != 0:
            return "No"
    
    return "Yes" 

w = input()
print(is_beautiful(w))