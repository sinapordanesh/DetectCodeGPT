def simple_dictionary(n, instructions):
    dictionary = set()
    result = []
    
    for instruction in instructions:
        if instruction.startswith("insert"):
            string = instruction.split()[1]
            dictionary.add(string)
        elif instruction.startswith("find"):
            string = instruction.split()[1]
            if string in dictionary:
                result.append("yes")
            else:
                result.append("no")
    
    return result

# Sample Input 1
n1 = 5
instructions1 = ["insert A", "insert T", "insert C", "find G", "find A"]
print(simple_dictionary(n1, instructions1))

# Sample Input 2
n2 = 13
instructions2 = ["insert AAA", "insert AAC", "insert AGA", "insert AGG", "insert TTT", 
                 "find AAA", "find CCC", "find CCC", "insert CCC", "find CCC", 
                 "insert T", "find TTT", "find T"]
print(simple_dictionary(n2, instructions2))