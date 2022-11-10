# fuctions

def hello_func():
    print("hello fuction!!")


hello_func()
#  print(len(hello_func()))
print(type(hello_func()))  # nonetype type


def Hey_fxn():
    return 'hey function'


Hey_fxn()
a = Hey_fxn()
print(a)

print(Hey_fxn().upper())
print(type(Hey_fxn()))  # str type
print(len(Hey_fxn()))


def hi_func(greeting):
    return '{} Function.'.format(greeting)


print(hi_func('Hi'))


def greet_func(greeting, name='You'):
    return '{}, {}'.format(greeting, name)


print(greet_func('Hi'))
print(greet_func('Hi', 'Akash'))


def student_info(*args, **kwargs):
    print(args)
    print(kwargs)

    print(type(args))
    print(type(kwargs))


student_info('math', 'art', name='John', age=22)


# Number of days in a month.First value placeholder for indexing purposes
month_days = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]


def is_leap(year):
    """Return True for leap year, False for non-leap years."""
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


def days_in_month(year, month):

    if not 1 <= month <= 12:
        return 'Invalid month'

    if month == 2 and is_leap(year):
        return 29
    return month_days[month]


print(is_leap(1700))
print(is_leap(2000))
print(days_in_month(1700, 2))
