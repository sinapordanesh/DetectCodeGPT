def minimum_years(string):
    result = float('inf')
    for i in range(1, len(string)):
        segments = [string[j:j+i] for j in range(0, len(string), i)]
        diff = max([int(segment) for segment in segments]) - min([int(segment) for segment in segments])
        result = min(result, diff)
    return result

# Sample Test Cases
print(minimum_years("11121314"))
print(minimum_years("123125129"))
print(minimum_years("119138"))