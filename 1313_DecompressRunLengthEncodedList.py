class Solution:
    def decompressRLElist(self, nums):
        l = []
        for i in range(0,len(nums),2):
            freq,num = nums[i],nums[i+1]
            l+=[num]*freq
        return l

class Solution:
    def decompressRLElist(self, nums):
        i = len(nums)-1
        while i>=0:
            nums+=[nums.pop(i)]*nums.pop(i-1)
            i-=2
        nums.reverse()
        return nums