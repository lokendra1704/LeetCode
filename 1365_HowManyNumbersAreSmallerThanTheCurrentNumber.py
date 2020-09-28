from collections import DefaultDict


class Solution:
    def smallerNumbersThanCurrent(self, nums):
        temp = sorted(nums)
        d = DefaultDict(list)
        for i in range(len(nums)):
            d[temp[i]].append(i)
        ans = []
        for i in range(len(nums)):
            ans.append(min(d[nums[i]]))
        return ans