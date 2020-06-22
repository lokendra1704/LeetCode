#Kadane's Algo
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        if not nums: return 0
        total = nums[0]
        mxm = nums[0]
        for j in range(1, len(nums)):
            i = nums[j]
            total = max(i, total + i)
            mxm = max(mxm, total)
        return mxm

#DivideAndConquer
