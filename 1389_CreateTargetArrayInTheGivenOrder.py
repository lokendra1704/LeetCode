from typing import List


class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        l = []
        for n,i in zip(nums,index):
            l.insert(i,n)
        return l