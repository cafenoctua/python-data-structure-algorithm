from typing import List
import random


def countingsort(nums: List[int], place: int) -> List[int]:
    count_list = [0] * 10

    for num in nums:
        index = int(num / place) % 10
        count_list[index] += 1

    for i in range(1, 10):
        count_list[i] += count_list[i-1]

    results = [0] * len(nums)
    i = len(nums) - 1
    while i >= 0:
        index = int(nums[i] / place) % 10
        results[count_list[index]-1] = nums[i]
        count_list[index] -= 1
        i -= 1

    return results


def radixsort(nums: List[int]) -> List[int]:
    max_num = max(nums)
    place = 1
    while place < max_num:
        nums = countingsort(nums, place)
        place *= 10

    return nums


if __name__ == "__main__":
    nums = [4, 3, 6, 2, 3, 4, 7]
    nums = [random.randint(0, 1000) for _ in range(10)]
    print(radixsort(nums))
