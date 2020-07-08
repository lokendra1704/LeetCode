class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        s = None
        results = []
        for i in range(len(nums)-2):
            if nums[i]>0:
                break
            if i>0 and nums[i]==nums[i-1]:
                continue
            l,r = i+1,len(nums)-1
            while l<r:
                s = nums[i]+nums[l]+nums[r]
                if s>0: r-=1
                elif s<0: l+=1
                else:
                    results.append([nums[i],nums[l],nums[r]])
                    l+=1
                    r-=1
                    while (nums[l]==nums[l-1] or nums[r]==nums[r+1]) and l<r:
                        if nums[l]==nums[l-1]: l+=1
                        if nums[r]==nums[r+1]: r-=1         
        return results