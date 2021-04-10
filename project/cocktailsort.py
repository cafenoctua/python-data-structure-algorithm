from typing import List
import random

def cocktailsort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    start_pos = 0
    end_pos = len_nums - 1
    swapped = True
    while swapped:
        swapped = False
        for i in range(start_pos, end_pos):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
                
        if not swapped:
            break

        swapped = False
        end_pos -= 1
        for i in range(end_pos-1, start_pos-1, -1):
            if nums[i] > nums[i+1]:
                nums[i], nums[i+1] = nums[i+1], nums[i]
                swapped = True
        start_pos += 1
    return nums

if __name__ == "__main__":
    nums = [2,5,1,7,8,3]
    nums = [random.randint(0, 100) for _ in range(10)]
    print(cocktailsort(nums))
