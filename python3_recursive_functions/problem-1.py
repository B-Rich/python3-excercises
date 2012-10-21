"""
Think of a recusive version of the function f(n) = 3 * n, i.e. the multiples of 3
"""

def showFactorsRecursively(n):
  """
  (int) -> list()
  show the factors of a number.

  This function should be recursive, but I am not sure
  how to make it recursive and get the results I am 
  looking for.
  """
  return [x for x in range(1,n+1) if n % x == 0]


def showFactors(n):
  """
  (int) -> list()
  show the factors of a number.
  """
  return [x for x in [1] + primes(n) if n%x == 0]

def primes(n):
  """
  (int) -> list()
  generate a list of prime numbers.
  start with a bottom bounds and a top bounds
  """
  r = [i if i%2 != 0 else 0 for i in list(range(0,n+1)) ]
  r[1] = 0
  r[2] = 2
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
print(showFactors(100))
print(showFactorsRecursively(100))
