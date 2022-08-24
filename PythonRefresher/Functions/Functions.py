"""
Functions
"""


def print_username(first_name, last_name):
    print(f"Hello {first_name}, {last_name}!")


def print_color_red():
    color = "Red"
    print(color)


def print_numbers(highest_number, lowest_number):
    print(highest_number)
    print(lowest_number)


def multiply_numbers(a, b):
    return a * b


def print_list(list_of_numbers):
    for x in list_of_numbers:
        print(x)


def buy_item(cost_of_item):
    return cost_of_item + add_tax_to_item(cost_of_item)


def add_tax_to_item(cost_of_item):
    current_tax_rate = .03
    return cost_of_item * current_tax_rate


print_username("Joeun", "Park")

color = "Blue"
print(color)
print_color_red()

print_numbers(lowest_number=3, highest_number=10)

solution = multiply_numbers(10, 6)
print(solution)

number_list = [1, 2, 3, 4, 5]
print_list(number_list)

final_cost = buy_item(50)
print(final_cost)
