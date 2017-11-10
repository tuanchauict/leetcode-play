from utils import evaluate


class Solution(object):
    def findShortestSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        m = {}
        mm = [[0, 0, 0]]
        ma = -1
        for (i, n) in enumerate(nums):
            mn = m.setdefault(n, [i, i, 0])
            m[n] = mn
            mn[2] += 1
            mn[1] = i

            if ma < mn[2]:
                mm = [mn]
                ma = mm[0][2]
            elif (ma == mn[2]):
                mm.append(mn)

        mi = mm[0][1] - mm[0][0]
        for t in mm[0:]:
            if t[1] - t[0] < mi:
                mi = t[1] - t[0]
        return mi + 1


s = Solution()
import random
nums = [random.randint(1, 100) for i in range(1000000)]
# nums = [1,2,2,3,1,4,2]
evaluate(s.findShortestSubArray, nums)
