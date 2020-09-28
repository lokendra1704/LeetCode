class Solution:
    def kidsWithCandies(self, nums, extraCandies):
        highest = max(nums)
        return [i+extraCandies>=highest for i in nums]