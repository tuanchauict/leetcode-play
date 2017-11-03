class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        count = 0
        for i in range(len(nums) - 1):
            for j in range(0, k):
                if i + j + 1 >= len(nums):
                    break
                if abs(nums[i] - nums[i + j + 1]) <= t:
                    count += 1
                    if count >= 2:
                        return True

        return False


import random
k = 1000
t = 0
nums = [i for i in range(k)]

s = Solution()
print(s.containsNearbyAlmostDuplicate(nums, k, t))
