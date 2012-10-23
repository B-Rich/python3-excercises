"""
Write a recursive function find_index(), which returns the index of a number in the Fibonacci sequence, if the number is an element of this sequence and returns -1 if the number is not contained in it, i.e. 

# # # # # # # # # # # # # # # # # # #
# Not sure what that is asking for  #
# # # # # # # # # # # # # # # # # # #
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

def find_index(x, guess = 1):
  """
  (int) -> int
  return index of a fibonacci sequence
  """
  while(x >= fibonacci(guess)):
    guess += 1
  return [fibonacci(i) for i in range(guess)]
 
print(fibonacci(10))
print(find_index(13))
