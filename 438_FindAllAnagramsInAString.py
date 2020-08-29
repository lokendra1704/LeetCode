#438
#Find All Anagrams in a String
#Speed: 89.41%
class Solution:
    def findAnagrams(self, s, p):
        n = len(s)
        m = len(p)
        if n<m:
            #print('False')
            return []
        d = [0]*26
        d1 = [0]*26
        result = []
        for i in range(m):
            d[ord(s[i])-ord('a')]+=1
            d1[ord(p[i])-ord('a')]+=1
        if d==d1:
            #print('True')
            result.append(0)
        for i in range(1,n-m+1):
            d[ord(s[i-1])-ord('a')]-=1
            d[ord(s[i+m-1])-ord('a')]+=1
            if d==d1:
                print('True')
                result.append(i)
        return result

print(Solution().findAnagrams("abacbabc","abc"))