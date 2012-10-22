"""
The Fibonacci numbers are hidden inside of Pascal's triangle. If you sum up the coloured numbers of the following triangle, you will get the 7th Fibonacci number:
"""

def printFib(x):
  for row in range(x):
    row += 1 # b/c zero index
    out = 0

    for col in range(row):
      col += 1 # b/c zero index
      out += fibViaPascal(row, col)

    print(out)

  return ""


def fibViaPascal(r, c):
  """
  print out pascals triangle
  """
  if(c < 1 or c > r):
    return 0
  
  if(c == 1 or c == r):
    return 1
  
  return fibViaPascal(r-1, c-1) + fibViaPascal(r-2, c+2) 


printFib(10)
