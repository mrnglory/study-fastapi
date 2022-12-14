"""
Sets are similar to lists but are unordered and cannot contain duplications
User curly brackets
"""


my_set = {1, 2, 3, 4, 5, 1, 2}
print(my_set)       # {1, 2, 3, 4, 5}
print(len(my_set))


for x in my_set:
    print(x)


my_set.discard(3)
print(my_set)
my_set.clear()
print(my_set)
my_set.add(6)
print(my_set)
my_set.update([7, 8])
print(my_set)
my_tuple = (1, 2, 3, 4, 5)
print(my_tuple[1])
my_tuple[1] = 100   # TypeError: 'tuple' object does not support item assignment
print(my_tuple)
