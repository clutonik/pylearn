from typing import List


def containsNearbyAlmostDuplicate(nums: List[int], k: int, t: int) -> bool:
    if len(nums) == 0:
        return False

    for i in range(0, len(nums)):
        for j in range(i+1, i+1+k):
            if j >= len(nums):
                break
            if abs(nums[i] - nums[j]) <= t and abs(i-j) <= k:
                return True

    return False


list1 = [1, 5, 9, 1, 5, 9]
k = 2
t = 3
print(list1)
print(containsNearbyAlmostDuplicate(list1, k, t))
