"""
The sum of the squares of two consecutive Fibonacci numbers is also a Fibonacci number, e.g. 2 and 3 are elements of the Fibonacci sequence and 2*2 + 3*3 = 13 corresponds to Fib(7). 
Use the previous function to find the position of the sum of the squares of two consecutive numbers in the Fibonacci sequence. 

Mathematical explanation:
Let a and b be two successive Fibonacci numbers with a prior to b. The Fibonacci sequence starting with the number "a" looks like this:
0              a
1              b
2          a + b	
3	  a + 2b
4 	 2a + 3b
5        3a + 5b
6        5a + 8b
We can see that the Fibonacci numbers appear as factors for a and b. The n-th element in this sequence can be calculated with the following formula: 
F(n) = Fib(n-1)* a + Fib(n) * b
From this we can conclude that for a natural number n, n>1, the following holds true:
Fib(2*n + 1) = Fib(n)**2 + Fib(n+1)**2
"""

from functools import lru_cache

@lru_cache(maxsize=None)
def fibonacci(x):
  """
  (int) -> int
  return fibonacci for int
  """
  if(x <= 1):
    return x
  return fibonacci(x-1) + fibonacci(x-2)

def fibonacciSequence(n):
  """
  (int) -> list
  return a fibonacci sequencenth up to nth index
  """
  return [fibonacci(x) for x in range(n)]

def find_index(x, guess = 1):
  """
  (int) -> int
  return index of a fibonacci sequence
  """
  while(x >= fibonacci(guess)):
    guess += 1
  fibList = fibonacciSequence(guess)
  if(fibList[-1] == x):
    return len(fibList) - 1
  return -1

def findSoSIndex(x,y):
  """
  (int, int) -> int
  returns the index of the sum of squares in the fibonacci
  function.
  """
  idx = find_index(x*x + y*y)
  if(idx != -1):
    return len(fibonacciSequence(idx)) - 1

  return -1
 
print(fibonacci(10))
print(find_index(13))
print(findSoSIndex(8, 13))
print(8*8 + 13*13, fibonacciSequence(13), ": length = ", len(fibonacciSequence(13)))
