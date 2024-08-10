def min_operations(s):
    count = 0
    while len(set(s)) > 1:
        new_s = ""
        for i in range(len(s) - 1):
            if s[i] == s[i+1]:
                new_s += s[i]
            else:
                new_s += s[i+1]
        s = new_s
        count += 1
    return count

# Test the function with the provided sample inputs
print(min_operations("serval"))
print(min_operations("jackal"))
print(min_operations("zzz"))
print(min_operations("whbrjpjyhsrywlqjxdbrbaomnw"))