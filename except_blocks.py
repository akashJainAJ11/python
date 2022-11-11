

try:
    f = open('testfile.txt')
except FileNotFoundError:
    print('sorry! This file does not exist')
except Exception:
    print("Sorry. Something went wrong")

finally:
    print("Executing Finally ...")
# else:
#     pass
# finally:
#     pass
