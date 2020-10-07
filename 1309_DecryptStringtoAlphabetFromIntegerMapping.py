class Solution:
    def freqAlphabets(self, s: str) -> str:
        i=0
        ans = ""
        while i<len(s):
            if i+2<len(s) and s[i+2]=="#":
                ans+=chr(int(s[i:i+2])+ord('a')-1)
                i+=3
            else:
                ans+=chr(int(s[i])+ord('a')-1)
                i+=1
        return ans


class Solution:
    def freqAlphabets(self, s: str) -> str:
        for i in range(26,0,-1): s = s.replace(str(i)+'#'*(i>9),chr(96+i))
        return s