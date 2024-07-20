n,k=map(int,input().split())
def replace(m):
  if m=="A":
    return "a"
  elif m=="B":
    return "b"
  else:
    return "c"
  
abc_str=list(input())
abc_str[k-1]=replace(abc_str[k-1])
abc_str="".join(abc_str)
print(abc_str)