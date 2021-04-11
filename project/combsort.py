from typing import List
import math
import random

def combsort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    gap = len_nums
    swapped = True
    while swapped or gap != 1:
        gap = int(gap / 1.3)
        if gap < 1:
            gap = 1
        swapped = False
        for i in range(0, len_nums - gap):
            if nums[i] > nums[i + gap]:
                nums[i], nums[i + gap] = nums[i + gap], nums[i]
                swapped = True
            
    return nums
        

if __name__ == "__main__":
    nums = [2, 9, 1, 8, 7, 3, 5]
    nums = [random.randint(0,100) for _ in range(10)]
    print(combsort(nums))