
if True:
    print("num is equal to 5")
else:
    print("num is not equal to 5")

# False values:
# False
# None
#  Zero of any numeric types
# any empty sequence. for example, '', (), {}
# any empty mapping. for example, {}

a = [1, 2, 3]
b = [1, 2, 3]

print(a == b)

print(id(a))
print(id(b))
print(a is b)

b = a
print(id(a))
print(id(b))
print(a is b)
