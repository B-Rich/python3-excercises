"""
The Fibonacci numbers are hidden inside of Pascal's triangle. If you sum up the coloured numbers of the following triangle, you will get the 7th Fibonacci number:
"""

def pascal(r, c):
  """
  print out pascals triangle
  """
  if(c == 1 or c >= r):
    return 1
  
  return pascal(r-1, c) + pascal(r-1, c-1)

