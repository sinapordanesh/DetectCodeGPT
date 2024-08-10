def can_form_bracket_sequence(N, strings):
    left_brackets = 0
    right_brackets = 0
    
    for string in strings:
        left_brackets += string.count('(')
        right_brackets += string.count(')')
        
    if left_brackets == right_brackets:
        return "Yes"
    else:
        return "No"