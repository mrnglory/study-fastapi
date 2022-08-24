"""
Dictionaries
"""


user_dictionary = {
    "username": "soju",
    "name": "joeun",
    "age": 24,
}

# print(user_dictionary)
# print(user_dictionary.get("username"))

user_dictionary["married"] = False
# print(user_dictionary)

# user_dictionary.pop("age")
# print(user_dictionary)

# user_dictionary.clear()
# print(user_dictionary)

# for x in user_dictionary:
#     print(x)

user_dictionary2 = user_dictionary
user_dictionary.pop("age")
print(user_dictionary2)



# del user_dictionary
# print(user_dictionary)      # NameError: name 'user_dictionary' is not defined


