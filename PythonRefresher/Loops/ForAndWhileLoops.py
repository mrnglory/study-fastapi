"""
for and while loops
"""


my_list = [1, 2, 3, 4, 5]

# print(my_list[0])
# print(my_list[1])
# print(my_list[2])
# print(my_list[3])
# print(my_list[4])

for iterator in my_list:
    print(iterator)

sum_of_for_loop = 0

for x in range(3, 6):
    sum_of_for_loop += x
print(sum_of_for_loop)


week = ["Monday", "Tuesday", "Wednesday", "Thursday"]
for day in week:
    print(f"Happy {day}!")


i = 0

while i < 5:
    i += 1
    if i == 3:
        continue
    print(i)
    if i == 4:
        break
else:
    print("i is now larger than or equal to 5")
