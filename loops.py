prims = [2, 3, 5, 7]
for prim in prims:
    print(prim)


# Prints out the numbers 0,1,2,3,4
for x in range(5):
    print(x)

# Prints out 3,4,5
for x in range(3, 6):
    print(x)

# Prints out 3,5,7
for x in range(3, 8, 2):
    print(x)


# ****************************************************************
i = 0
while i < 10:
    print(i)
    i += 1


count = 0
while count < 10:
    print(count)
    count += 1
    if count > 5:
        break


for x in range(10):
    if x % 2 == 0:
        continue
    print(x)

count = 0
while(count < 5):
    print(count)
    count += 1
else:
    print("count value reached %d" % (count))

# Prints out 1,2,3,4
for i in range(1, 10):
    if(i % 5 == 0):
        break
    print(i)
else:
    print("this is not printed because for loop is terminated because of break but not due to fail in condition")
