class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        size = len(nums)
        def solver(i,last=float("inf")):
            #Top Down Approach
            "i here is the (last_index + 1) so we wil check nums[i-1] because (i-1) will be the last index"
            
            if i<=0: return 0
            
            elif nums[i-1]>=last:                       # (=) means strictly Increasing.
                return solver(i-1,last)                 #When the current solution isn't a part of LIS

            elif nums[i-1]<last:
                return max(1+solver(i-1,nums[i]),       #When the current number is a part of LIS
                            solver(i-1,last))           #When the current solution isn't a part of LIS
            
        solver(size) #Mind that second parameter should pe passed with value of float("inf").

    def lengthofLIS(self, nums):
        #Bottom Up Approach
        pass
