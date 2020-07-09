class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        l,r = [1]*len(nums), [1]*len(nums) 
        for i in range(1,len(nums)):
            l[i] = l[i-1]*nums[i-1]
            r[~i] = r[~(i-1)]*nums[~(i-1)]
        for i in range(len(nums)):
            nums[i] = l[i]*r[i]
        return nums