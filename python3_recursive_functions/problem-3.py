"""
Write a function which implements the Pascal's triangle:
"""

def printPascalTriangle(r):
  for row in range(r):
    row += 1 # b/c zero index
    pad = int((r - row))
    print(" " * pad, end=" ")

    for col in range(row):
      col += 1 # b/c zero index
      pad = int((r - row) / 2)
      print(pascal(row, col), end=" ")
      #print("pascal({0}, {1})".format(row, col))

    print("\n")

  return ""


def pascal(r, c):
  """
  print out pascals triangle
  """
  if(c == 1 or c >= r):
    return 1
  
  return pascal(r-1, c) + pascal(r-1, c-1)


print(printPascalTriangle(10))
