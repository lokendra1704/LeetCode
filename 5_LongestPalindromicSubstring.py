class Solution:
    def longestPalindrome(self, s: str) -> str:
        longest = ""
        size = len(s)
        for i in range(size):
            #Odd Palindrome
            left,right = i,i
            ls = ""
            while 0<=left<size and 0<=right<size and s[left]==s[right]:
                if left==right:
                    ls = s[left]
                else:
                    ls = s[left] + ls + s[right]
                left-=1
                right+=1
            #Even Palindrome
            left,right = i,i+1
            rs = ""
            while 0<=left<size and 0<=right<size and s[left]==s[right]:
                rs = s[left] + rs + s[right]
                left-=1
                right+=1
            temp = ls if len(ls)>len(rs) else rs
            longest = temp if len(temp)>len(longest) else longest
        return longest