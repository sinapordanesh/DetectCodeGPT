s = input()

def first_A(s):
  for i in range(len(s)):
    if s[i] == "A":
      return i
    
def last_Z(s):
  for i in range(len(s)):
    if s[-(i+1)] == "Z":
      return -(i+1)+len(s)
    
print(last_Z(s) - first_A(s) + 1)