
# Local, Enclosing, Global, Built-in
import builtins
print(dir(builtins))
m = min([14, 25, 78, 96, 3, 29, 24, 18])
print(m)


x = 'global x'


def test():
    global x
    y = 'local y'
    x = 'local x'
    print(y)
    print(x)


test()
# print(y)   #error
print(x)


def test01(z):
    print(z)


test01('local z')

# enclosing


n = 'global n'


def outer():
    n = 'outer n'

    def inner():
        n = 'inner n'
        print(n)
    inner()
    print(n)


outer()
print(n)
