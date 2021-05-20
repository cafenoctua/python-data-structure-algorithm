from typing import List
import random


def gnomesort(nums: List[int]) -> List[int]:
    len_nums = len(nums)

    # # my answer
    # for i in range(len_nums-1):
    #     if nums[i] > nums[i+1]:
    #         nums[i], nums[i+1] = nums[i+1], nums[i]
    #         for j in range(i, 0, -1):
    #             if nums[j] < nums[j-1]:
    #                 nums[j], nums[j-1] = nums[j-1], nums[j]
    #             else:
    #                 break
    # return nums

    # answer
    index = 0
    while index < len_nums:
        if index == 0:
            index += 1
        if nums[index] >= nums[index-1]:
            index += 1
        else:
            nums[index], nums[index-1] = nums[index-1], nums[index]
            index -= 1
    return nums


if __name__ == "__main__":
    nums = [2, 5, 1, 8, 7, 3]
    nums = [random.randint(0, 100) for _ in range(10)]
    print(gnomesort(nums))
