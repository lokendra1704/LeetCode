#567
#Speed: 95.78%
class Solution:
    def checkInclusion(self, s2: str, s1: str) -> bool:
        n = len(s1)
        m = len(s2)
        if n<m:
            return False
        d = [0]*26
        d1= [0]*26
        t = ord('a')
        for i in range(m):
            d[ord(s1[i])-t]+=1
            d1[ord(s2[i])-t]+=1
        if d==d1:
            return True
        for i in range(1,n-m+1):
            d[ord(s1[i-1])-t]-=1
            d[ord(s1[i+m-1])-t]+=1
            if d==d1:
                return True
        return False