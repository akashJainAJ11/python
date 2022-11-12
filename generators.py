
def square_numbers(nums):
    result = []
    for i in nums:
        result.append(i*i)
    return result


my_nums = square_numbers([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(my_nums)

my_nums01 = [x*x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9]]
print(my_nums01)


def square_num(nums):
    for y in nums:
        yield(y*y)


my_nums02 = square_num([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(list(my_nums02))
