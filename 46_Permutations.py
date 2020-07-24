'''
class Solution:
    def permute(self, nums):
        l = []
        def perm(s, left, right):
            if left == right:
                l.append(s.copy())
                return
            for i in range(left, right):
                s[left], s[i] = s[i], s[left]
                perm(s, i+1, right)
                s[left], s[i] = s[i], s[left]
        perm(nums, 0, len(nums))
        return l

'''
class Solution:
    def permute(self, nums):
        ret = []

        def helper(temp):
            if len(temp) == len(nums):
                ret.append(temp + [])
                return
            for i in nums:
                if i not in temp:
                    temp.append(i)
                    helper(temp)
                    temp.pop()

        helper([])
        return ret

x = Solution().permute(['1','2','3','4'])
print(x)