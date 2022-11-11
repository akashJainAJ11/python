
# f = open('lec02.py', 'r')

# print(f.name)
# f.close()

with open('lec02.py', 'r') as f:

    size_to_read = 100
    # f_contents = f.read(100)
    # f_contents = f.read()
    f_contents = f.read(size_to_read)

    while len(f_contents) > 0:
        print(f_contents, end='')
        f_contents = f.read(size_to_read)


# write mode

# with open('test.txt', 'w') as f:
#     f.write('Test')
#     f.write('Test')

# Copy- text content of file

# with open('test.txt', 'r') as rf:
#     with open('test01.txt', 'w') as wf:
#         for line in rf:
#             wf.write(line)


# copy photo content of file
# with open('test.jpg', 'rb') as rf:
#     with open('test01.jpg', 'wb') as wf:
#         for line in rf:
#             wf.write(line)
