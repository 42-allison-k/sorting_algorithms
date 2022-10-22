from random import randint


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


rand_list_3 = []
for i in range(1, 10):
    i = randint(-100, 100)
    rand_list_3.append(i)

rand_num = randint(-100, 100)

print(searchinsert(rand_list_3, rand_num))
print(randint(-100, 100))
print(rand_list_3)
