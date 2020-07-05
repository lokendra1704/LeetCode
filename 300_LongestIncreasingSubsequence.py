from functools import lru_cache

class Solution:
    def iLIS(self, nums):
        size = len(nums)  #largest_Index
        nums = dict(enumerate(nums))
        nums[-1] = -float("inf")

        @lru_cache(None)
        def sulver(i, prev_index): #sulver(0,-1)
            if i >= size:
                return 0
            elif nums[i] <= nums[prev_index]:
                return sulver(i + 1, prev_index)
            elif nums[i] > nums[prev_index]:
                return max(1 + sulver(i + 1, i), sulver(i + 1, prev_index))
        return sulver(0,-1)


x = Solution().iLIS([4,10,4,3,8,9])
print(x)