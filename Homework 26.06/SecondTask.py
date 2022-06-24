# Exercise 2: Print the sum of the current number and the previous number
# Write a program to iterate the first 10 numbers and in each iteration, print the sum of the current and previous number.

current_number = int(input("Enter a number! "))

for current_number in range(current_number, current_number + 10):
    previous_number = current_number - 1
    sum = current_number + previous_number
    print("Current Number: {} Previous Number: {} Their Sum is: {}".format(current_number, previous_number, sum))