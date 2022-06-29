# Exercise 12: Calculate income tax for the given income by adhering to the below rules

# Taxable Income	Rate (in %)
# First $10,000	    0
# Next $10,000	    10
# The remaining	    20

# For example, suppose the taxable income is 45000 the income tax payable is
# 10000*0% + 10000*10%  + 25000*20% = $6000.

taxable_income = 45000
tax_payable = 0

if taxable_income <= 10000:
    tax_payable = 0
elif taxable_income <= 20000:
    
