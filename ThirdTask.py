# Exercise 3: Print characters from a string that are present at an even index number
# Write a program to accept a string from the user and display characters that are present at an even index number.

string = input("Enter whatever! ")

for i in range(len(string)):
    if i % 2 == 0:
        print(string[i])
