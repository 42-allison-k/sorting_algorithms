from random import randint
from time import time


def searchinsert(nums, target):
    start = 0
    end = len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
            return start + searchinsert(nums[start:], target)
        elif nums[mid] > target:
            end = mid - 1
            return searchinsert(nums[: end + 1], target)
    return start


def linear_search(nums, target):
    for i, val in enumerate(nums):
        if val == target:
            return i


def create_list(list_len):
    rand_list = []
    for i in range(list_len):
        i = randint(-100, 100)
        rand_list.append(i)
        rand_list.sort()

    return rand_list


if __name__ == "__main__":
    rand_num = randint(-100, 100)
    rand_list_1 = create_list(100)
    rand_list_2 = create_list(10000)
    rand_list_3 = create_list(1000000)
    b_search_times = []
    l_search_times = []

    search_start = time()
    searchinsert(rand_list_1, rand_num)
    b_search_times.append(time() - search_start)

    search_start = time()
    searchinsert(rand_list_2, rand_num)
    b_search_times.append(time() - search_start)

    search_start = time()
    searchinsert(rand_list_3, rand_num)
    b_search_times.append(time() - search_start)

    search_start = time()
    linear_search(rand_list_1, rand_num)
    l_search_times.append(time() - search_start)

    search_start = time()
    linear_search(rand_list_2, rand_num)
    l_search_times.append(time() - search_start)

    search_start = time()
    linear_search(rand_list_3, rand_num)
    l_search_times.append(time() - search_start)

    print(b_search_times)
    print(l_search_times)
