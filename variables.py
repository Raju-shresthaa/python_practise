x = 3
y = 2
z = x + y
print(z)
# print(id(y))

x = 2
y = 2
z = x + y
print(z)
# print(type(x))
# print(id(x))
# print(id(y))
# Variables are changeable

# string variables
name = 'youtube'
new_name = 'youtube'
# print(id(name))
# print(id(new_name))
# print(name)
# print(name[0])
# print(name[-2])
# print(name[1:3])

# lists
nums = [1, 4, 5, 7, 23]
y = 1
# print(id(y))
# print(id(nums[0]))
print(id(nums))
print(type(nums))
print(nums)

# question1
list1 = [1, 2, 3, 4, 5]
list2 = [1, 2, 3, 4, 5]
print(id(list2))
print(id(list1))

# list1[0] = 5
list1.append(10)
print(list1)
print(id(list1))

# retieve data from list2 and append all data in list1
for i in list2:
    list1.append(i)
    # print(list1)
# print(list1)

# add two lists inside a new list
new_list = [list1, list2]
print(new_list)

# TUPLE
# tuple is immutable, execution of tuple is faster than list
tup = (1, 2, 3, 4, 5)

# sets
# immutable
set = {1, 2, 3, 4, 5,98,789}
print(set)
