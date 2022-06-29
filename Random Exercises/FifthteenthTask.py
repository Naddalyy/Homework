# Exercise 15: Write a function called exponent(base, exp) that returns an int value of base raises to the power of exp.
# Note here exp is a non-negative integer, and the base is an integer.

def exponent(base, exp):
    n = base ** exp
    print(n)

# Testing:
exponent(2, 5) # == 32
exponent(5, 4) # == 625