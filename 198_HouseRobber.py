from functools import lru_cache
class Solution:
    def rob(self, nums):
        dp = {i:0 for i in range(len(nums)+1)}
        dp[-1]=0
        for k in range(1,len(dp)-1):
            i = k-1
            dp[k] = max(dp[k-2]+nums[i],dp[k-1])
        return dp[len(nums)]

print(Solution().rob([1,2,3,1]))