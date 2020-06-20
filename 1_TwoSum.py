#Two-pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {v:i for i,v in enumerate(nums)}
        for i in range(len(nums)):
            comp = target - nums[i]
            temp = d.get(comp,-1)
            if temp!=-1 and temp!=i:
                return [i,temp]

#Single Pass
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in d:
                return [d[complement],i]
            d[nums[i]]=i
