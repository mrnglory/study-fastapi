"""
Function Assignment
- Create a function that takes 3 parameters(firstname, lastname, age) and returns a dictionary based on those values
"""


def return_user_info(firstname, lastname, age):
    return {
        "firstname": firstname,
        "lastname": lastname,
        "age": age
    }


print(return_user_info(firstname="joeun", lastname="park", age=24))
