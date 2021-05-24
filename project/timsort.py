from typing import List
import random

def mergesort(nums: List[int], l: int, m: int, r: int) -> List[int]:
    len_left, len_right = m - l + 1, r - m
    left, right = [], []
    for i in range(0, len_left):
        left.append(nums[l + i])
    for i in range(0, len_right):
        right.append(nums[m + 1 + i])

    i, j, k = 0, 0, l
    while i < len_left and j < len_right:
        if left[i] <= right[j]:
            nums[k] = left[i]
            i += 1
        else:
            nums[k] = right[j]
            j += 1
        k += 1
    
    while i < len_left:
        nums[k] = left[i]
        i += 1
        k += 1
    
    while j < len_right:
        nums[k] = right[j]
        j += 1
        k += 1

    return nums

def insertionsort(nums: List[int], left: int, right: int) -> List[int]:
    for i in range(left + 1, right + 1):
        temp = nums[i]
        j = i - 1
        while j >= left and nums[j] > temp:
            nums[j+1] = nums[j]
            j -= 1

        nums[j+1] = temp

    return nums


def timsort(nums: List[int], size: int = 32) -> List[int]:
    n = len(nums)
    for i in range(0, n, size):
        insertionsort(nums, i, min((i + 31), (n - 1)))
    
    while size < n:
        for left in range(0, n, 2 * size):
            mid = left + size - 1
            right = min((left + 2 * size - 1), (n - 1))
            mergesort(nums, left, mid, right)
        size = 2 * size
    return nums

if __name__ == "__main__":
    nums = [random.randint(0, 1000) for _ in range(1000)]
    print(timsort(nums))