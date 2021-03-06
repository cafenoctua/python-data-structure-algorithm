from typing import List
import random


def partition(nums: List[int], low: int, high: int) -> int:
    i = low - 1
    pivot = nums[high]
    for j in range(low, high):
        if nums[j] <= pivot:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
    nums[i+1], nums[high] = nums[high], nums[i+1]
    return i + 1


def quick_sort(nums: List[int]) -> List[int]:
    def _quick_sort(nums: List[int], low: int, high: int) -> None:
        if low < high:
            partition_index = partition(nums, low, high)
            _quick_sort(nums, low, partition_index-1)
            _quick_sort(nums, partition_index+1, high)

    _quick_sort(nums, 0, len(nums)-1)
    return nums

if __name__ == "__main__":
    nums = [1,8,3,9,4,5,7]
    nums = [random.randint(0, 1000) for _ in range(100)]
    print(quick_sort(nums))

