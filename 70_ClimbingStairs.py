'''
Speed: 94.76%
Memory: 5.68%
'''
class Solution:
    def climbStairs(self, n: int) -> int:
        a,b = 1,1
        if n==1:
            return 1
        for i in range(2,n+1):
            t = a+b
            a,b = b,t
        return t