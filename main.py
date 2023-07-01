from time import time

import numpy as np
from numpy.random import randint


def print_time(func):
    def _wrapper(*args, **kwargs):
        start_time = time()
        func(*args, **kwargs)
        print(f"{func.__name__}: {time() - start_time} seconds")

    return _wrapper


@print_time
def oneline(nums):
    return [n for n in nums if n % 2]


@print_time
def classic_for(nums):
    ret_arr = []
    for i in nums:
        if i % 2:
            ret_arr.append(i)
    return ret_arr


@print_time
def while_method(nums):
    i = 0
    ret_arr = []
    while i < len(nums):
        if nums[i] % 2:
            ret_arr.append(i)
        i += 1
    return ret_arr


@print_time
def enumeration(nums):
    ret_arr = []
    for i, val in enumerate(nums):
        if val % 2:
            ret_arr.append(val)
    return ret_arr


@print_time
def for_range(nums):
    ret_arr = []
    for i in range(len(nums)):
        if nums[i] % 2:
            ret_arr.append(nums[i])
    return ret_arr


@print_time
def numpy_with_conversion(nums):
    np_nums = np.array(nums)
    return [n for n in np_nums if n % 2]


@print_time
def iterations(nums):
    iterator = iter(nums)
    ret_arr = []
    try:
        while True:
            i = next(iterator)
            if i % 2:
                ret_arr.append(nums[i])
    except StopIteration:
        return ret_arr


@print_time
def mapping(nums):
    ret_arr = []

    def check_odd(i):
        if i % 2:
            ret_arr.append(nums[i])

    for _ in map(check_odd, nums):
        pass
    return ret_arr


@print_time
def bitwise(nums):
    return [n for n in nums if n & 1]


if __name__ == '__main__':
    num_arr = list(randint(0, 16777215, size=16777215))
    oneline(num_arr)
    classic_for(num_arr)
    while_method(num_arr)
    enumeration(num_arr)
    for_range(num_arr)
    numpy_with_conversion(num_arr)
    iterations(num_arr)
    mapping(num_arr)
    bitwise(num_arr)
