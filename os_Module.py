import os

from datetime import datetime

# os.mkdir(path)

# os.rename('old.txt', 'new.txt)

print(os.stat('lec08.py'))
print(os.stat('lec08.py').st_size)

# print(dir(os))
# print(os.getcwd())


mod_time = os.stat('lec08.py').st_mtime
print(datetime.fromtimestamp(mod_time))

for dirpath, dirnames, filenames in os.walk('/Users/Dell/Desktop/'):
    print('Current Path:', dirpath)
    print('Directories:', dirnames)
    print('Files:', filenames)
    print()
