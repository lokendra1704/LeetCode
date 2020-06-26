#Sliding Window Optimized
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        size = len(s)
        ans = 1
        i=0
        seen = {}
        for j in range(size):
            if s[j] in seen:
                i = max(seen[s[j]]+1,i)
            ans = max(ans,j-i+1)
            seen[s[j]] = j     
        return ans


#Sliding Window
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if not s: return 0
        size = len(s)
        ans = 1
        i,j=0,0
        window = set()
        while i<size and j<size:
            if s[j] not in window:
                window.add(s[j])
                ans = max(ans,j-i+1)
                j+=1
            else:
                window.remove(s[i])
                i+=1
                
        return ans