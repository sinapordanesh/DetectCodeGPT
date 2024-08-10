def parse(s, left, target_stack):
  if s[left] == "[":
    target_stack.append("]")
  if s[left] == "(":
    target_stack.append(")")
  
  if s[left] == "]":
    if target_stack and target_stack[-1] == "]":
      target_stack.pop()
    else:
      return False

  if s[left] == ")":
    if target_stack and target_stack[-1] == ")":
      target_stack.pop()
    else:
      return False

  left += 1
  if left == len(s):
    if target_stack:
      return False
    else:
      return True

  else:
    return parse(s, left, target_stack)

while True:
  s = input()
  if s == ".":
    break

  if parse(s, 0, []):
    print("yes")
  else:
    print("no")
