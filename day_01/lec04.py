# list

names = ['ironman', 'harry', 'money', 'sunny']

print(names)
print(type(names))
print(len(names))
print(names[0])
print(names[-1])

print(names.sort())

names.reverse()
print(names)


names.append('Aman')
print(names)

names.insert(0, 'ravi')
print(names)

names.remove('ravi')
print(names)

names.pop()  # by default delete last value
print(names)

names.pop(0)
print(names)

a = names.pop(1)
print(a)


nums = [12, 96, 235, 4, 25, 35, 75, 46, 79, 4]
nums.sort()
print(nums)

nums.sort(reverse=True)
print(nums)

numbers = [12, 96, 235, 4, 25, 35, 75, 46, 79, 4]
b = sorted(numbers)
print(b)


print(min(nums))
print(max(nums))
print(sum(nums))

print(nums.index(79))

print(79 in nums)
print(85 in nums)

for name in names:
    print(name)

for name in enumerate(names):
    print(name)


name = ' - '.join(names)
print(name)

new_name = name.split(' - ')
print(new_name)

# list are mutable
# tuples are immutable

# mutable
list_1 = [1, 2, 3, 4, 5]
list_2 = list_1
print(list_1)
print(list_2)

list_1[0] = 'abc'

print(list_1)
print(list_2)

print(type(list_1[0]))
print(type(list_1[1]))

# immutable

tuple_1 = (1, 2, 3, 4, 5, 6)
tuple_2 = tuple_1

print(tuple_1)
print(tuple_2)

# tuple[0] = 9
# print(tuple_1)
# print(tuple_2)

tuple_3 = ('abc', 2, 3, 4, 5, 6)
print(tuple_3)
print(type(tuple_3[0]))
print(type(tuple_3[1]))


# sets
set_1 = {1, 2, 3, 4, 4, 5, 6}
print(set_1)  # print multi element only single time

set_2 = {1, 'money', 'sunny', 'ravi', 'aman', 'aman'}
print(set_2)  # print in random order


set_3 = {1, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13}

set_4 = {10, 20, 18, 46, 11, 18, 7}

print(set_3.difference(set_4))
print(set_3.intersection(set_4))
print(set_3.union(set_4))


# Empty list

empty_list = []
empty_list = list()


# Empty tuple
empty_tuple = ()
empty_tuple = tuple()

# Empty sets

empty_set = {}  # this is not right . it is dict
empty_sets = set()


# dict

student = {'name': 'Aman', 'age': 25, 'course': ['math', 'cs']}

student['phone'] = '5631353653'
print(student)
student['name'] = 'ravi'
print(student['name'])

student.update({'name': 'sunil', 'age': 20, 'course': ['physics', 'ec']})

del student['age']
a = student.pop('phone')
print(a)
print(student)
print(len(student))
print(student.keys())
print(student.values())

for key, value in student.items():
    print(key, value)
