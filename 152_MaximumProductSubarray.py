class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        mn,mx = nums[0],nums[0]
        r=nums[0]
        for i in range(1,len(nums)):
            k = nums[i]
            if k<0:
                mn,mx = mx,mn
            mn = min(k,mn*k)
            mx = max(k,mx*k)
            r = max(r,mx)
        return r