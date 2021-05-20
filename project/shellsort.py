from typing import List
import random


def shellsort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    gap = len_nums // 2
    # shuffled = True
    # i = 0
    # while shuffled or gap > 0:
    #     shuffled = False
    #     i += gap
    #     if i > len_nums-1:
    #         gap = int(gap / 2)
    #         i = gap
    #     if nums[i] < nums[i - gap]:
    #         nums[i], nums[i - gap] = nums[i - gap], nums[i]
    #         shuffled = True
    #         j = i - gap
    #         while j > 0:
    #             if nums[j] < nums[j - gap]:
    #                 nums[j], nums[j - gap] = nums[j - gap], nums[j]
    #                 j -= gap
    #             else:
    #                 break

    # ans
    while gap > 0:
        for i in range(gap, len_nums):
            temp = nums[i]
            j = i
            while j >= gap and nums[j-gap] > temp:
                nums[j] = nums[j-gap]
                j -= gap
            nums[j] = temp
        gap //= 2

    return nums


if __name__ == "__main__":
    nums = [5, 6, 9, 2, 3]
    nums = [random.randint(0, 100) for _ in range(10)]
    print(shellsort(nums))
