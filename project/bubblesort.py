import random
from typing import List

def bubblesort(nums: List[int]) -> List[int]:
    len_nums = len(nums)
    for i in range(len_nums):
        for j in range(1, len_nums - i):
            if nums[j-1] > nums[j]:
                x = nums[j]
                nums[j] = nums[j-1]
                nums[j-1] = x
    
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 100) for _ in range(10)]
    print(bubblesort(nums))
