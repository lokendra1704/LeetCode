from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums = [i-1 for i in  nums]
        nums.sort()
        return nums[-1]*nums[-2]