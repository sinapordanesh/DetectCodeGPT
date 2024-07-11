from collections import defaultdict
def main():
  def primes(n):
    is_prime = [True] * (n + 1)
    is_prime[0] = is_prime[1] = False
    for i in range(2, int(n ** (1 / 2)) + 1):
      if is_prime[i]:
        for j in range(i * i, n + 1, i):
          is_prime[j] = False
    return [i for i in range(n + 1) if is_prime[i]]
  
  prime_list = primes(100000)
  solvers = [[] for _ in range(100001)]
  for p in prime_list:
    for i in range(p, 100001, p):
      solvers[i].append(p)
   
  n = int(input())
  a_list = list(map(int, input().split()))
  parent = [i for i in range(100001)]
  
  def find(x):
    if x == parent[x]:
      return x
    parent[x] = find(parent[x])
    return parent[x]
  
  for i, v in enumerate(a_list):
    p_rep = find(min(solvers[v]))
    for s in solvers[v]:
      parent[find(s)] = p_rep
    parent[find(v)] = p_rep
  
  dic = defaultdict(set)
  for i, v in enumerate(a_list):
    dic[find(v)].add(i)
  
  a_list.sort()
  for i, v in enumerate(a_list):
    if i not in dic[find(v)]:
      print(0)
      break
  else:
    print(1)

main()

