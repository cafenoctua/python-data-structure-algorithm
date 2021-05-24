from typing import List
import random

def mergesort(nums: List[int]) -> List[int]:
    if len(nums) <= 1:
        return nums
    center = len(nums) // 2
    nums_l = nums[:center]
    nums_r = nums[center:]
    mergesort(nums_l)
    mergesort(nums_r)

    i = j = k = 0
    while i < len(nums_l) and j < len(nums_r):
        if nums_l[i] <= nums_r[j]:
            nums[k] = nums_l[i]
            i += 1
        else:
            nums[k] = nums_r[j]
            j += 1
        k += 1
    
    while i < len(nums_l):
        nums[k] = nums_l[i]
        i += 1
        k += 1
    
    while j < len(nums_r):
        nums[k] = nums_r[j]
        j += 1
        k += 1

    return nums
if __name__ == "__main__":
    nums = [5,4,1,8,7,3,2,9]
    nums = [random.randint(0,100) for _ in range(99)]
    print(mergesort(nums))