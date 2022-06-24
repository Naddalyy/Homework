# Exercise 1: Calculate the multiplication and sum of two numbers
# Given two integer numbers return their product only if the product is equal to or lower than 1000, else return their sum.

a = int(input("Enter the first number! "))
b = int(input("Enter the second number! "))

def product_or_sum(a, b):
    product = a * b
    sum = a + b

    if product <= 1000:
        return(product)
    else:
        return(sum)

result = product_or_sum(a, b)
print(result)