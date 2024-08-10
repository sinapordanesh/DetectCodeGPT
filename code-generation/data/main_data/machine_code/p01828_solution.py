def can_form_original_company_name(S, T):
    mixed_name = ""
    for i in range(len(S)):
        mixed_name += S[i] + T[i]
    
    if mixed_name == S:
        return "Yes"
    else:
        return "No"

# Sample Input 1
print(can_form_original_company_name("acmicpc", "tsukuba"))

# Sample Input 2
print(can_form_original_company_name("hoge", "moen"))

# Sample Input 3
print(can_form_original_company_name("abcdefg", "xacxegx"))