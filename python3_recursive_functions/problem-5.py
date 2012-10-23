"""
Implement a recursive function in Python for the sieve of Eratosthenes.
The sieve of Eratosthenes is a simple algorithm for finding all prime numbers up to a specified integer. It was created by the ancient Greek mathematician Eratosthenes. 
The algorithm to find all the prime numbers less than or equal to a given integer n:
Create a list of integers from two to n: 2, 3, 4, ..., n
Start with a counter i set to 2, i.e. the first prime number
Starting from i+i, count up by i and remove those numbers from the list, i.e. 2*i, 3*i, 4*i, aso..
Find the first number of the list following i. This is the next prime number.
Set i to the number found in the previous step
Repeat steps 3 and 4 until i is greater than n. (As an improvement: It's enough to go to the square root of n)
All the numbers, which are still in the list, are prime numbers
You can easily see, that we would be inefficient, if we strictly used this algorithm, e.g. we will try to remove the multiples of 4, although they have been already removed by the multiples of 2. So it's enough to produce the multiples of all the prime nummbers up to the square root of n. We can recursively create these sets. 
"""

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

print(primes(1000))
