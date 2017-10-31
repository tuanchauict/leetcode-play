import time

class Solution:
    def reversePairs(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        t0 = time.time()
        ma = max(nums)
        mi = min(nums)
        print(time.time() - t0)
        t1 = time.time()
        pivot = (ma + mi) >> 1
        # print(pivot)
        count = 0
        for i in range(len(nums) - 1):
            n = nums[i]
            # print('n', n, n >= pivot)
            if n < pivot:
                continue
            for j in range(i, len(nums)):
                # print('nn', nums[j])
                if n >  nums[j] << 1:
                    count += 1

        print(time.time() - t1)
        return count


nums = [1, 3, 2, 3, 1]
nums = [2,4,3,5,1]
import random
nums = [random.randint(0, 2**32) for i in range(5000)]
sol = Solution()
number = sol.reversePairs(nums)
print(number)
