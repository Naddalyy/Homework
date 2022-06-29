# Exercise 4: Remove first n characters from a string
# Write a program to remove characters from a string starting from zero up to n and return a new string.

def remove_chars(word, n):
    word = word[n:]
    print(word)

remove_chars("Hello", 2) # llo.
remove_chars("This is a test.", 5) # is a test.