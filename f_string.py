
from datetime import datetime
first_name = 'Akash'
last_name = 'Jain'

sectence_01 = 'My name is {} {}'.format(first_name, last_name)
print(sectence_01)

sectence_02 = f'My name is {first_name} {last_name}'
print(sectence_02)


person = {'name': 'John', 'age': 25}

sectence_03 = 'My name is {} and I am {} years old'.format(
    person['name'], person['age'])
print(sectence_03)

sectence_04 = f"My name is {person['name']} and I am {person['age']} years old"
print(sectence_04)


calculation = f'4 times 11 is equal to {4 * 11}'
print(calculation)

for n in range(1, 11):
    sectence_05 = f'The value is {n:02}'
    print(sectence_05)

pi = 3.14159265

sectence_06 = f'Pi is equal to {pi:.4f}'
print(sectence_06)


birthday = datetime(2003, 10, 15)

sectence_07 = f'rahul has a birthday on {birthday:%B %d, %Y}'
print(sectence_07)
