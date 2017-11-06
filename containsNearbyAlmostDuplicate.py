class Solution:
    def containsNearbyAlmostDuplicate(self, nums, k, t):
        """
        :type nums: List[int]
        :type k: int
        :type t: int
        :rtype: bool
        """
        if not nums or k < 0 or t < 0:
            return False

        mi = min(nums)
        ma = max(nums)
        div = t + 1
        number_groups = (ma - mi) // div + 1

        gs = {}

        for i, n in enumerate(nums):
            gs.setdefault((n - mi) // div, []).append((i, n))

        for i, g in gs.items():

            for (j, p1) in enumerate(g):

                if len(g) > 1:
                    for p2 in g[j + 1:]:
                        if abs(p1[0] - p2[0]) <= k:
                            return True

                if i < number_groups - 1 and (i + 1) in gs:
                    for p3 in gs[i + 1]:
                        if abs(p1[0] - p3[0]) <= k and abs(p1[1] - p3[1]) <= t:
                            return True

        return False

    def sol2(self, nums, k, t):
        if not nums:
            return False
        if k <= 0:
            return False
        if t < 0:
            return False

        for i, n1 in enumerate(nums):

            for j, n2 in enumerate(nums[i + 1:i + k + 1]):
                if abs(n1 - n2) <= t:
                    return True

        # for i in range(len(nums) - 1):
        #     for j in range(0, k):
        #         if i + j + 1 >= len(nums):
        #             break
        #         if abs(nums[i] - nums[i + j + 1]) <= t:
        #             count += 1
        #             if count >= 1:
        #                 return True

        return False


import random
from utils import evaluate

k = 10000
t = 0
nums = [i for i in range(k)]

# nums = [random.randint(0, k) for i in range(k)]
# print(nums)
nums = [11, 3, 10, 19, 11, 17, 2, 6, 18, 11]
k = 1
nums = [2147483647, -2147483645]
k = 1
t = 5
s = Solution()
# evaluate(s.sol3, nums, k, t)
evaluate(s.containsNearbyAlmostDuplicate, nums, k, t)
evaluate(s.sol2, nums, k, t)
