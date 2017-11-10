class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        # Sliding window solution
        def possible(guess, nums, k):
            count, left = 0, 0
            for right, num in enumerate(nums):
                while num - nums[left] > guess:
                    left += 1
                count += right - left
            return count >= k

        nums.sort()
        left, right = 0, nums[-1] - nums[0] + 1
        while left < right:
            mid = left + (right - left) / 2
            if possible(mid, nums, k):
                right = mid
            else:
                left = mid + 1
        return left

    def bf(self, nums, k):
        s = set()
        for i, n in enumerate(nums[:-1]):
            for nn in nums[i + 1:]:
                s.add(abs(nn - n))

        l = list(s)
        l.sort()
        return l[k - 1]

nums = [1, 3, 1]
k = 2

s = Solution()
print(s.bf(nums, k))