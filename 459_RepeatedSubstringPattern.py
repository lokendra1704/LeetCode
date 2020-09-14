class Solution:
    def repeatedSubstringPattern(self, s):
        if not s:
            return False
        # if set(s):
        #     return True
        n = len(s)//2
        if not n&1: n-=1
        for i in range(2,n+1):
            lensub = len(s)//i
            if len(set([s[k:k+lensub] for k in range(0,len(s),lensub)]))==1:
                return True
        return False

print(Solution().repeatedSubstringPattern("abab"))
print(Solution().repeatedSubstringPattern("abcabcabz"))