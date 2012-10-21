"""
Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
"""

def showFactors(n):
  """
  (int) -> list()
  show the factors of a number.
  """
  return 0 

def primes(n):
  """
  (int) -> list()
  generate a list of prime numbers.
  start with a bottom bounds and a top bounds
  """
  r = list(range(0,n+1))
  r[1] = 0
  bottom = 2
  top = n
  while(bottom * bottom <= top):
    while(bottom <= top):
      if(r[top] and bottom * top <= n):
        r[bottom*top] = 0
      top -= 1
    top=n
    bottom += 1
  return [x for x in r if x]

print(primes(100))
