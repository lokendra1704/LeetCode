class Solution:
    @staticmethod
    def permute(nums):
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

x = Solution.permute(['a','b','c'])
print(x)