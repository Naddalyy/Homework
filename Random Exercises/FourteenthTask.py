# Exercise 14: Print downward Half-Pyramid Pattern with Star (asterisk)
# * * * * *  
# * * * *  
# * * *  
# * *  
# *

rows = 5

for i in range(rows + 1, 0, -1):               # Does -1 reverse the loop?
    for j in range(0, i - 1):
        print("*", end=" ")
    print(" ")