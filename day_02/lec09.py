# import sys
# sys.path.append('/..../lec08')

import os
import calendar
import datetime
import math
import random
import lec08 as my_module
# from lec08 import find_index

subject = ['math', 'physics', 'chemistry', 'BCE', 'BME']

# index = lec08.find_index(subject, 'BCE')
index = my_module.find_index(subject, 'BCE')
print(index)


subject = ['math', 'physics', 'chemistry', 'BCE', 'BME']

random_sub = random.choice(subject)
print(random_sub)


rads = math.radians(90)
print(math.sin(rads))


today = datetime.datetime.today()
print(today)

print(calendar.isleap(2015))

print(os.getcwd())
