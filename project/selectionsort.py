from typing import List
import random

def selectionsort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(0, len_nums):
        min_idx = i
        for j in range(i+1, len_nums):
            if nums[min_idx] > nums[j]:
                min_idx = j
            
        nums[i], nums[min_idx] = nums[min_idx], nums[i]

    return nums

if __name__ == "__main__":
    nums = [2,5,1,8,7,3]
    nums = [random.randint(0, 100) for _ in range(10)]
    print(selectionsort(nums))