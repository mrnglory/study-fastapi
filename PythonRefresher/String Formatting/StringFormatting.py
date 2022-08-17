"""
String Formatting
"""


first_name = "Soju"
print("Hi " + first_name)
print(f"Hi {first_name}")

sentence = "Hi {} {}"
last_name = 'Joeun'
print(sentence.format(first_name, last_name))
print(f"Hi {first_name} {last_name} ~!")