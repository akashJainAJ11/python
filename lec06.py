# for

nums = [1, 2, 3, 4, 5]

for num in nums:
    if num == 5:
        print('found!')
        break
    print(num)


for num in nums:
    if num == 5:
        print('found!')
        continue
    print(num)

for num in nums:
    for letter in 'abc':
        print(num, letter)

for i in range(10):
    print(i)


# while

x = 0

while x < 10:
    print(x)
    x += 1
