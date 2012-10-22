"""
Write a recursive Python function that returns the sum of the first n integers. 
"""

def factorial(x):
  """
  Just for fun.
  """
  if(x <= 1):
    return x

  return x * factorial(x-1)

def sumOfFirstIntegers(x):
  """
  (x) -> int
  for the number x, sum the first integers
  """
  if(x <= 0):
    return x 

  return x + sumOfFirstIntegers(x-1)

def sumOfFirstNIntegers(x,n):
  """
  (x, n) -> int
  for the number x, sum the first n integers
  """
  if(n <= 0):
    return n 

  return n + sumOfFirstNIntegers(x, n-1)

print(sumOfFirstIntegers(10))
print(sumOfFirstNIntegers(100, 10))
print(factorial(10))
