# Exercise 6: Display numbers divisible by 5 from a list
# Iterate the given list of numbers and print only those numbers which are divisible by 5.

given_list = [10, 20, 33, 46, 55]

for num in given_list:
    if num % 5 == 0:
        print(num)