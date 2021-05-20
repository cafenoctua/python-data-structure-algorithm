from typing import List
import random


def countingsort(nums: List[int]) -> List[int]:
    max_nums = max(nums)
    count_list = [0 for _ in range(max_nums+1)]

    for num in nums:
        count_list[num] += 1

    for i in range(1, len(count_list)):
        count_list[i] += count_list[i-1]

    results = nums.copy()
    for i in range(len(nums)-1, 0, -1):
        num = nums[i]
        results[count_list[num]-1] = num
        count_list[num] -= 1

    return results


if __name__ == "__main__":
    nums = [4, 3, 6, 2, 3, 4, 7]
    nums = [random.randint(0, 100) for _ in range(10)]
    print(countingsort(nums))
