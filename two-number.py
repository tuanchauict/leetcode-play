from utils import evaluate


class Solution(object):
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if not nums:
            return []
        d = {}

        for i, n in enumerate(nums):
            if (target - n) in d:
                return [d[target - n], i]
            d[n] = i

        return []

s = Solution()
nums = [3,3]
target = 6
evaluate(s.twoSum, nums, target)