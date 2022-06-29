# Exercise 9: Check Palindrome Number
# Write a program to check if the given number is a palindrome number.

# Notes: 
# Using slice operation [start:end:step] / Step value "-1" reverses a string.

given_number = input(("Enter a number. "))

if (given_number == given_number[::-1]):
    print(("Original number {} \nThis number is a palindrome number.").format(given_number))
else:
    print(("Original number {} \nThis number is not a palindrome number.").format(given_number))