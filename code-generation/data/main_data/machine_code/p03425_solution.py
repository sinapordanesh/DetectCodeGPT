def count_ways(N, names):
    count = 0
    first_letters = set()
    for name in names:
        first_letters.add(name[0])
    
    if 'M' in first_letters and 'A' in first_letters and 'R' in first_letters:
        count += 1
    if 'M' in first_letters and 'A' in first_letters and 'C' in first_letters:
        count += 1
    if 'M' in first_letters and 'A' in first_letters and 'H' in first_letters:
        count += 1
    if 'M' in first_letters and 'R' in first_letters and 'C' in first_letters:
        count += 1
    if 'M' in first_letters and 'R' in first_letters and 'H' in first_letters:
        count += 1
    if 'M' in first_letters and 'C' in first_letters and 'H' in first_letters:
        count += 1
    if 'A' in first_letters and 'R' in first_letters and 'C' in first_letters:
        count += 1
    if 'A' in first_letters and 'R' in first_letters and 'H' in first_letters:
        count += 1
    if 'A' in first_letters and 'C' in first_letters and 'H' in first_letters:
        count += 1
    if 'R' in first_letters and 'C' in first_letters and 'H' in first_letters:
        count += 1
    
    return count

N = 5
names = ["CHOKUDAI", "RNG", "MAKOTO", "AOKI", "RINGO"]
print(count_ways(N, names))