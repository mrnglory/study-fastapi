"""
- You have $50
- You buy an item that is $15
- With a tax of 3%
- print how much money you have left
"""

money = 50
item = 15
tax = .03

money_left = money - item * (1 + tax)

print(money_left)
