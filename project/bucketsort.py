from typing import List
import random


def insertionsort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    # my answer
    # index = 0
    # for i in range(len_nums-1):
    #     if nums[i] > nums[i + 1]:
    #         tmp_num = nums[i]
    #         for j in range(i - 1, 0, -1):
    #             if tmp_num < nums[j]:
    #                 nums[i], nums[j] = nums[j], tmp_num
    #                 break

    # return nums

    # answer
    for i in range(1, len_nums):
        temp = nums[i]
        j = i - 1
        while j >= 0 and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = temp

    return nums


def bucketsort(nums: List[int]) -> List[int]:
    max_num = max(nums)
    len_nums = len(nums)
    size = max_num // len_nums
    bucket = [[] for _ in range(size)]
    for num in nums:
        i = int(num / size)
        if i < size:
            bucket[i].append(num)
        else:
            bucket[size-1].append(num)

    for i in range(size):
        insertionsort(bucket[i])

    results = []
    for i in range(size):
        results += bucket[i]
    return results


if __name__ == "__main__":
    nums = [1, 7, 3, 2, 8, 5]
    nums = [random.randint(0, 100) for _ in range(10)]
    print(bucketsort(nums))
