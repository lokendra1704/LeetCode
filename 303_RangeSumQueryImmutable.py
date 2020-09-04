class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = list(accumulate(nums))

    def sumRange(self, i: int, j: int) -> int:
        ans = self.nums[j]
        if i>0:
            ans-=self.nums[i-1]
        return ans
