# Exercise 5: Check if the first and last number of a list is the same
# Write a function to return True if the first and last number of a given list is same. If numbers are different then return False.

numbers_x = [10, 20, 30, 40, 10]
numbers_y = [75, 65, 35, 75, 30]


def same_or_not_numbers_x():
    if numbers_x[0] == numbers_x[-1]:
        return True
    else:
        return False

def same_or_not_numbers_y():
    if numbers_y[0] == numbers_y[-1]:
        return True
    else:
        return False

print("The first and last element of numbers_x is:", numbers_x[0], numbers_x[-1])
print("The first and last element of numbers_y is:", numbers_y[0], numbers_y[-1])