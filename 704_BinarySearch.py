class Solution:
    @staticmethod
    def search(nums, target):
        low,high = 0,len(nums)-1
        while low<high:
            mid = high - (high-low)//2
            temp = nums[mid]
            if nums[mid]==target:
                return mid
            elif target>nums[mid]:
                low = mid
            else:
                high = mid-1
        return -1

x = Solution.search([-1,0,3,5,9,12],2)