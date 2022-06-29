# Exercise 11: Write a Program to extract each digit from an integer in the reverse order.
# For example, If the given int is 7536, the output shall be “6 3 5 7“, with a space separating the digits.

given_int = int(input("Enter a number. "))
rev = 0

while (given_int > 0):
    a = given_int % 10
    rev = rev * 10 + a
    given_int = given_int // 10

print(rev)

# Digits need to be seperated by spaces! How do I do this with integers?
# What is the math???