

class Duck:

    def quack(self):
        print('Quack, quack')

    def fly(self):
        print('Flap, Flap!')


class Person:

    def quack(self):
        print("I'm Quacking like a Duck!")

    def fly(self):
        print("I'm Flapping my Arms!")


# def quack_and_fly(thing):
#     # Not Duck-Typed(Non-Pythonic)
#     if isinstance(thing, Duck):
#         thing.quack()
#         thing.fly()
#     else:
#         print("This has to be a Duck!")
#     print()

def quack_and_fly(thing):
    # EAFP (pythonic)
    try:
        thing.quack()
        thing.fly()
    except AttributeError as e:
        print(e)

    print()


d = Duck()
quack_and_fly(d)

p = Person()
quack_and_fly(p)


person = {'name': 'John', 'age': 25, 'job': 'Programmer'}


# LBYL (Non-pythonic)
if 'name' in person and 'age' in person and 'job' in person:
    print("I'm {name}. I'm {age} years old and an a {job}".format(**person))

else:
    print("Missing some keys")

    # EAFP (pythonic)
try:
    print("I'm {name}. I'm {age} years old and an a {job}".format(**person))
except KeyError as e:
    print("Missing {} key".format(e))


my_list = [1, 2, 3, 4, 5, 6]

# non pythonic
if len(my_list) >= 6:
    print(my_list[5])
else:
    print("That index does not exist")

# pythonic
try:
    print(my_list[5])
except IndexError:
    print("That index does not exist")
