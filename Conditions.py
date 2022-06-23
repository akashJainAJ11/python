x = 2
print(x == 2)
print(x == 3)
print(x < 3)


x = 2
if x == 2:
    print("x equals two!")
else:
    print("x does not equal to two.")

x = [1, 2, 3]
y = [1, 2, 3]
print(x == y)  # Prints out True
print(x is y)  # Prints out False


print(not False)  # Prints out True
print((not False) == (False))  # Prints out False
